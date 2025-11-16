import random
import time

class OBDSimulator:
    def __init__(self):
        self.pids = {
            '010D': 'Vehicle Speed',
            '010C': 'Engine RPM', 
            '0105': 'Coolant Temperature',
            '010B': 'Intake Manifold Pressure',
            '010F': 'Intake Air Temperature',
            '0111': 'Throttle Position',
            '0104': 'Calculated Load Value',
            '0142': 'Control module voltage',
            '0101': 'DTC Status',
            '0103': 'Fuel System Status',
            '0106': 'Short Term Fuel Trim',
            '0107': 'Long Term Fuel Trim',
            '0110': 'MAF Air Flow Rate',
            '0113': 'Oxygen Sensors Present'
        }
        
    def generate_response(self, pid):
        """Generate different responses for each PID"""
        if pid == '010D':  # Vehicle Speed
            speed = random.randint(0, 120)
            return f"41{pid} {speed:02X}", f"Speed: {speed} km/h"
            
        elif pid == '010C':  # Engine RPM
            rpm = random.randint(800, 3500)
            rpm_bytes = (rpm * 4)
            return f"41{pid} {rpm_bytes//256:02X} {rpm_bytes%256:02X}", f"RPM: {rpm}"
            
        elif pid == '0105':  # Coolant Temperature
            temp = random.randint(75, 105)
            return f"41{pid} {temp + 40:02X}", f"Coolant Temp: {temp}°C"
            
        elif pid == '010B':  # Intake Manifold Pressure
            pressure = random.randint(20, 100)
            return f"41{pid} {pressure:02X}", f"MAP: {pressure} kPa"
            
        elif pid == '010F':  # Intake Air Temperature
            air_temp = random.randint(15, 45)
            return f"41{pid} {air_temp + 40:02X}", f"Air Temp: {air_temp}°C"
            
        elif pid == '0111':  # Throttle Position
            throttle = random.randint(0, 100)
            return f"41{pid} {throttle:02X}", f"Throttle: {throttle}%"
            
        elif pid == '0104':  # Calculated Load
            load = random.randint(10, 90)
            return f"41{pid} {load:02X}", f"Engine Load: {load}%"
            
        elif pid == '0142':  # Control Module Voltage
            voltage = random.randint(12800, 14500)
            return f"41{pid} {voltage//256:02X} {voltage%256:02X}", f"Voltage: {voltage/1000}V"
            
        elif pid == '0101':  # DTC Status
            status = random.randint(0, 255)
            return f"41{pid} {status:02X}", f"DTC Status: {status:08b}"
            
        elif pid == '0103':  # Fuel System Status
            status = random.choice([0x08, 0x10, 0x18])
            return f"41{pid} {status:02X}", f"Fuel System: {'Closed Loop' if status == 0x08 else 'Open Loop'}"
            
        else:
            return "NO DATA", "Unsupported PID"
    
    def simulate_obd_connection(self):
        """Simulate OBD-II communication with better print output"""
        print("OBD-II Simulator Started...")
        print("=" * 60)
        
        while True:
            try:
                # Pick a random PID to simulate
                pid = random.choice(list(self.pids.keys()))
                
                # Generate response
                hex_response, readable_value = self.generate_response(pid)
                
                # Print all the details
                print(f"📡 PID Request: {pid}")
                print(f"📋 Parameter: {self.pids[pid]}")
                print(f"🔧 Hex Response: {hex_response}")
                print(f"📊 Value: {readable_value}")
                print("-" * 40)
                
                time.sleep(2)
                
            except KeyboardInterrupt:
                print("\n🛑 Simulator stopped")
                break

# Run the simulator
if __name__ == "__main__":
    sim = OBDSimulator()
    sim.simulate_obd_connection()