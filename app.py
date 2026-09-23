import streamlit as st
import math

# Page setup
st.set_page_config(page_title="Mechanical Engineering Calculator", page_icon="⚙️", layout="centered")

st.title("⚙️ Mechanical Engineering Calculator")
st.caption("A multi-module web calculator for mechanical engineering calculations.")

# Sidebar navigation
module = st.sidebar.selectbox(
    "Select Module",
    [
        "1. Mechanics",
        "2. Strength of Materials",
        "3. Thermodynamics",
        "4. Fluid Mechanics",
        "5. Thermal Engineering",
        "6. Machine Design"
    ]
)

# Helper function to display results
def show_result(topic, formula, result, unit=""):
    st.markdown("---")
    st.subheader(f"📌 {topic}")
    st.latex(formula)
    st.success(f"**Calculated Result:** {result:.4f} {unit}")


# ================= 1. Mechanics =================
if module == "1. Mechanics":
    st.header("1. Mechanics")
    sub = st.selectbox("Select Calculation", ["Force", "Work", "Power", "Kinetic Energy"])

    if sub == "Force":
        m = st.number_input("Mass (m) [kg]", min_value=0.0, value=10.0, step=0.5)
        a = st.number_input("Acceleration (a) [m/s²]", min_value=0.0, value=2.5, step=0.1)
        if st.button("Calculate Force"):
            show_result("Force", r"F = m \cdot a", m * a, "N")

    elif sub == "Work":
        f = st.number_input("Force (F) [N]", min_value=0.0, value=100.0, step=5.0)
        d = st.number_input("Displacement (d) [m]", min_value=0.0, value=5.0, step=0.5)
        if st.button("Calculate Work"):
            show_result("Work Done", r"W = F \cdot d", f * d, "J")

    elif sub == "Power":
        w = st.number_input("Work Done (W) [J]", min_value=0.0, value=500.0, step=10.0)
        t = st.number_input("Time (t) [s]", min_value=0.01, value=10.0, step=0.5)
        if st.button("Calculate Power"):
            show_result("Power", r"P = \frac{W}{t}", w / t, "W")

    elif sub == "Kinetic Energy":
        m = st.number_input("Mass (m) [kg]", min_value=0.0, value=20.0, step=1.0)
        v = st.number_input("Velocity (v) [m/s]", min_value=0.0, value=4.0, step=0.5)
        if st.button("Calculate Kinetic Energy"):
            ke = 0.5 * m * (v ** 2)
            show_result("Kinetic Energy", r"KE = \frac{1}{2} m v^2", ke, "J")


# ================= 2. Strength of Materials =================
elif module == "2. Strength of Materials":
    st.header("2. Strength of Materials")
    sub = st.selectbox("Select Calculation", ["Stress", "Strain", "Young's Modulus"])

    if sub == "Stress":
        f = st.number_input("Force/Load (F) [N]", min_value=0.0, value=5000.0, step=50.0)
        a = st.number_input("Cross-sectional Area (A) [m²]", min_value=0.00001, value=0.02, step=0.001, format="%.5f")
        if st.button("Calculate Stress"):
            show_result("Stress", r"\sigma = \frac{F}{A}", f / a, "Pa (N/m²)")

    elif sub == "Strain":
        dl = st.number_input("Change in Length (ΔL) [m]", min_value=0.0, value=0.002, step=0.0005, format="%.5f")
        l = st.number_input("Original Length (L) [m]", min_value=0.001, value=1.5, step=0.1)
        if st.button("Calculate Strain"):
            show_result("Strain", r"\varepsilon = \frac{\Delta L}{L}", dl / l, "(dimensionless)")

    elif sub == "Young's Modulus":
        stress = st.number_input("Stress (σ) [Pa]", min_value=0.0, value=200000.0, step=1000.0)
        strain = st.number_input("Strain (ε)", min_value=0.000001, value=0.001, step=0.0001, format="%.6f")
        if st.button("Calculate Young's Modulus"):
            show_result("Young's Modulus", r"E = \frac{\sigma}{\varepsilon}", stress / strain, "Pa")


# ================= 3. Thermodynamics =================
elif module == "3. Thermodynamics":
    st.header("3. Thermodynamics")
    sub = st.selectbox("Select Calculation", ["Heat Transfer", "Work Done", "Thermal Efficiency"])

    if sub == "Heat Transfer":
        m = st.number_input("Mass (m) [kg]", min_value=0.0, value=5.0, step=0.5)
        c = st.number_input("Specific Heat Capacity (c) [J/kg·K]", min_value=0.0, value=4184.0, step=10.0)
        dt = st.number_input("Temperature Change (ΔT) [K or °C]", value=25.0, step=1.0)
        if st.button("Calculate Heat Transfer"):
            show_result("Heat Transfer", r"Q = m \cdot c \cdot \Delta T", m * c * dt, "J")

    elif sub == "Work Done":
        p = st.number_input("Constant Pressure (P) [Pa]", min_value=0.0, value=101325.0, step=1000.0)
        dv = st.number_input("Change in Volume (ΔV) [m³]", value=0.05, step=0.01)
        if st.button("Calculate Work Done"):
            show_result("Work Done", r"W = P \cdot \Delta V", p * dv, "J")

    elif sub == "Thermal Efficiency":
        w = st.number_input("Net Work Output (W) [J]", min_value=0.0, value=300.0, step=10.0)
        qin = st.number_input("Heat Input (Qin) [J]", min_value=0.01, value=1000.0, step=10.0)
        if st.button("Calculate Efficiency"):
            if w > qin:
                st.error("Work output cannot exceed heat input.")
            else:
                eff = (w / qin) * 100
                show_result("Thermal Efficiency", r"\eta = \frac{W}{Q_{in}} \times 100", eff, "%")


# ================= 4. Fluid Mechanics =================
elif module == "4. Fluid Mechanics":
    st.header("4. Fluid Mechanics")
    sub = st.selectbox("Select Calculation", ["Pressure", "Reynolds Number", "Flow Velocity", "Discharge"])

    if sub == "Pressure":
        rho = st.number_input("Fluid Density (ρ) [kg/m³]", min_value=0.0, value=1000.0, step=10.0)
        h = st.number_input("Fluid Depth/Height (h) [m]", min_value=0.0, value=10.0, step=0.5)
        if st.button("Calculate Pressure"):
            p = rho * 9.81 * h
            show_result("Hydrostatic Pressure", r"P = \rho \cdot g \cdot h", p, "Pa")

    elif sub == "Reynolds Number":
        rho = st.number_input("Fluid Density (ρ) [kg/m³]", min_value=0.0, value=1000.0, step=10.0)
        v = st.number_input("Flow Velocity (v) [m/s]", min_value=0.0, value=2.0, step=0.1)
        d = st.number_input("Pipe Diameter (D) [m]", min_value=0.001, value=0.05, step=0.01)
        mu = st.number_input("Dynamic Viscosity (μ) [Pa·s]", min_value=0.00001, value=0.001, step=0.0001, format="%.5f")
        if st.button("Calculate Reynolds Number"):
            re = (rho * v * d) / mu
            show_result("Reynolds Number", r"Re = \frac{\rho \cdot v \cdot D}{\mu}", re, "(dimensionless)")

    elif sub == "Flow Velocity":
        q = st.number_input("Discharge (Q) [m³/s]", min_value=0.0, value=0.05, step=0.005)
        a = st.number_input("Pipe Area (A) [m²]", min_value=0.0001, value=0.02, step=0.001)
        if st.button("Calculate Velocity"):
            show_result("Flow Velocity", r"v = \frac{Q}{A}", q / a, "m/s")

    elif sub == "Discharge":
        a = st.number_input("Pipe Area (A) [m²]", min_value=0.0, value=0.02, step=0.001)
        v = st.number_input("Flow Velocity (v) [m/s]", min_value=0.0, value=2.5, step=0.1)
        if st.button("Calculate Discharge"):
            show_result("Discharge", r"Q = A \cdot v", a * v, "m³/s")


# ================= 5. Thermal Engineering =================
elif module == "5. Thermal Engineering":
    st.header("5. Thermal Engineering")
    sub = st.selectbox("Select Calculation", ["Heat Conduction", "COP", "Heat-Engine Efficiency"])

    if sub == "Heat Conduction":
        k = st.number_input("Thermal Conductivity (k) [W/m·K]", min_value=0.0, value=0.8, step=0.1)
        a = st.number_input("Surface Area (A) [m²]", min_value=0.0, value=12.0, step=0.5)
        dt = st.number_input("Temperature Difference (ΔT) [K or °C]", value=15.0, step=1.0)
        dx = st.number_input("Wall Thickness (dx) [m]", min_value=0.001, value=0.15, step=0.01)
        if st.button("Calculate Conduction Rate"):
            q = (k * a * abs(dt)) / dx
            show_result("Heat Conduction Rate", r"Q = \frac{k \cdot A \cdot \Delta T}{\Delta x}", q, "W")

    elif sub == "COP":
        cooling = st.number_input("Cooling/Heating Effect [W or J]", min_value=0.0, value=3500.0, step=50.0)
        work = st.number_input("Work Input [W or J]", min_value=0.01, value=1000.0, step=50.0)
        if st.button("Calculate COP"):
            show_result("Coefficient of Performance", r"\text{COP} = \frac{Q_{effect}}{W_{in}}", cooling / work, "")

    elif sub == "Heat-Engine Efficiency":
        th = st.number_input("Source Temperature (TH) [K]", min_value=0.1, value=600.0, step=10.0)
        tl = st.number_input("Sink Temperature (TL) [K]", min_value=0.1, value=300.0, step=10.0)
        if st.button("Calculate Carnot Efficiency"):
            if tl >= th:
                st.error("Sink temperature (TL) must be strictly less than source temperature (TH).")
            else:
                eff = (1 - (tl / th)) * 100
                show_result("Carnot Efficiency", r"\eta = \left(1 - \frac{T_L}{T_H}\right) \times 100", eff, "%")


# ================= 6. Machine Design =================
elif module == "6. Machine Design":
    st.header("6. Machine Design")
    sub = st.selectbox("Select Calculation", ["Torque", "Shaft Power", "Shaft Diameter"])

    if sub == "Torque":
        p = st.number_input("Power (P) [W]", min_value=0.0, value=15000.0, step=500.0)
        n = st.number_input("Shaft Speed (N) [RPM]", min_value=1.0, value=1440.0, step=10.0)
        if st.button("Calculate Torque"):
            t = (60 * p) / (2 * math.pi * n)
            show_result("Torque", r"T = \frac{60 \cdot P}{2 \pi N}", t, "N·m")

    elif sub == "Shaft Power":
        t = st.number_input("Torque (T) [N·m]", min_value=0.0, value=100.0, step=5.0)
        n = st.number_input("Shaft Speed (N) [RPM]", min_value=0.0, value=1440.0, step=10.0)
        if st.button("Calculate Shaft Power"):
            power = (2 * math.pi * n * t) / 60
            show_result("Shaft Power", r"P = \frac{2 \pi N T}{60}", power, "W")

    elif sub == "Shaft Diameter":
        t = st.number_input("Torque (T) [N·m]", min_value=0.0, value=250.0, step=10.0)
        tau = st.number_input("Allowable Shear Stress (τ) [Pa]", min_value=1.0, value=40000000.0, step=1000000.0)
        if st.button("Calculate Diameter"):
            d = ((16 * t) / (math.pi * tau)) ** (1 / 3)
            show_result("Shaft Diameter", r"d = \left(\frac{16 T}{\pi \tau}\right)^{\frac{1}{3}}", d, "m")
            st.info(f"Equivalent diameter in millimeters: **{d * 1000:.2f} mm**")
            
