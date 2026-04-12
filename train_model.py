"""
weather_prediction_app/train_model.py
=====================================
This script:
1. Creates synthetic weather data
2. Trains a Random Forest model
3. Saves the model and scaler
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

def create_dataset():
    """
    Creates synthetic weather data for training.
    In a real project, you would load historical data from a CSV.
    """
    np.random.seed(42)
    n_samples = 5000
    
    # Generate realistic weather features
    data = {
        # Temperature (Celsius)
        'temperature': np.random.uniform(-10, 40, n_samples),
        
        # Humidity (%)
        'humidity': np.random.uniform(20, 100, n_samples),
        
        # Pressure (hPa)
        'pressure': np.random.uniform(980, 1050, n_samples),
        
        # Wind Speed (km/h)
        'wind_speed': np.random.uniform(0, 50, n_samples),
        
        # Cloud Cover (%)
        'cloud_cover': np.random.uniform(0, 100, n_samples),
        
        # Visibility (km, scaled 0-10)
        'visibility': np.random.uniform(1, 10, n_samples),
    }
    
    # Create target: Next hour temperature prediction
    # Based on a realistic formula with some noise
    data['target_temperature'] = (
        data['temperature'] * 0.85 +           # Current temp has strong effect
        (100 - data['humidity']) * 0.08 +       # Lower humidity = higher temp
        (data['pressure'] - 1000) * 0.15 +      # Pressure affects temp
        data['wind_speed'] * -0.05 +            # Wind slightly reduces temp
        np.random.normal(0, 2, n_samples)       # Random noise
    )
    
    df = pd.DataFrame(data)
    
    # Create data directory if not exists
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/weatherHistory.csv', index=False)
    
    print(f"✅ Created dataset with {len(df)} records")
    return df

def train_model():
    """
    Main training function
    """
    print("=" * 50)
    print("🌤️  WEATHER PREDICTION MODEL TRAINING")
    print("=" * 50)
    
    # 1. Create or load dataset
    print("\n📊 Step 1: Loading dataset...")
    df = create_dataset()
    
    # 2. Prepare features and target
    print("\n🔧 Step 2: Preparing features...")
    features = ['temperature', 'humidity', 'pressure', 'wind_speed', 'cloud_cover', 'visibility']
    X = df[features]
    y = df['target_temperature']
    
    print(f"   Features: {features}")
    print(f"   Samples: {len(X)}")
    
    # 3. Split data
    print("\n✂️ Step 3: Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print(f"   Training: {len(X_train)} samples")
    print(f"   Testing: {len(X_test)} samples")
    
    # 4. Scale features
    print("\n📏 Step 4: Scaling features...")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    print("   ✅ Features scaled")
    
    # 5. Train model
    print("\n🤖 Step 5: Training Random Forest model...")
    model = RandomForestRegressor(
        n_estimators=100,
        max_depth=15,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train_scaled, y_train)
    print("   ✅ Model trained")
    
    # 6. Evaluate
    print("\n📈 Step 6: Evaluating model...")
    y_pred_train = model.predict(X_train_scaled)
    y_pred_test = model.predict(X_test_scaled)
    
    train_rmse = np.sqrt(mean_squared_error(y_train, y_pred_train))
    test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))
    train_r2 = r2_score(y_train, y_pred_train)
    test_r2 = r2_score(y_test, y_pred_test)
    
    print(f"   Training RMSE: {train_rmse:.4f}°C")
    print(f"   Testing RMSE: {test_rmse:.4f}°C")
    print(f"   Training R²: {train_r2:.4f}")
    print(f"   Testing R²: {test_r2:.4f}")
    
    # 7. Feature importance
    print("\n🎯 Feature Importance:")
    importance = model.feature_importances_
    for feat, imp in sorted(zip(features, importance), key=lambda x: x[1], reverse=True):
        print(f"   {feat}: {imp:.4f}")
    
    # 8. Save model
    print("\n💾 Step 7: Saving model...")
    os.makedirs('model', exist_ok=True)
    joblib.dump(model, 'model/weather_model.pkl')
    joblib.dump(scaler, 'model/scaler.pkl')
    print("   ✅ model/weather_model.pkl saved")
    print("   ✅ model/scaler.pkl saved")
    
    print("\n" + "=" * 50)
    print("🎉 TRAINING COMPLETE!")
    print("=" * 50)

if __name__ == '__main__':
    train_model()
