import streamlit as st
import math

st.set_page_config(
    page_title="Mechanical Engineering Calculator",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ Complete Mechanical Engineering Calculator")
st.markdown("A comprehensive tool for core Mechanical Engineering computations.")

# ----------------- SIDEBAR NAVIGATION -----------------
module = st.sidebar.selectbox(
    "Select Engineering Module",
    [
        "1. Mechanics",
        "2. Strength of Materials",
        "3. Thermodynamics",
        "4. Fluid Mechanics",
        "5. Thermal Engineering",
        "6. Machine Design"
    ]
)

# ================= 1. MECHANICS =================
if module == "1. Mechanics":
    st.header("1. Mechanics")
    sub_calc = st.radio(
        "Choose Calculation:",
        ["Force", "Work Done", "Power", "Kinetic Energy"],
        horizontal=True
    )

    if sub_calc == "Force":
        st.subheader("Force Calculation ($F = m \\times a$)")
        col1, col2 = st.columns(2)
        with col1:
            m = st.number_input("Mass (m) in kg", min_value=0.0, value=10.0, step=0.1)
        with col2:
            a = st.number_input("Acceleration (a) in m/s²", value=9.81, step=0.01)
        if st.button("Calculate Force"):
            force = m * a
            st.success(f"Force ($F$) = **{force:.4f} N**")

    elif sub_calc == "Work Done":
        st.subheader("Work Done ($W = F \\times d \\times \\cos(\\theta)$)")
        col1, col2, col3 = st.columns(3)
        with col1:
            f = st.number_input("Applied Force (F) in N", value=50.0, step=1.0)
        with col2:
            d = st.number_input("Displacement (d) in meters", value=5.0, step=0.5)
        with col3:
            theta = st.number_input("Angle θ (degrees)", value=0.0, step=1.0)
        if st.button("Calculate Work"):
            rad = math.radians(theta)
            work = f * d * math.cos(rad)
            st.success(f"Work Done ($W$) = **{work:.4f} J**")

    elif sub_calc == "Power":
        st.subheader("Power ($P = W / t$)")
        col1, col2 = st.columns(2)
        with col1:
            w = st.number_input("Work Done (W) in Joules", value=1000.0, step=10.0)
        with col2:
            t = st.number_input("Time (t) in seconds", min_value=0.001, value=5.0, step=0.5)
        if st.button("Calculate Power"):
            power = w / t
            st.success(f"Power ($P$) = **{power:.4f} W** ({power/1000:.3f} kW)")

    elif sub_calc == "Kinetic Energy":
        st.subheader("Kinetic Energy ($KE = \\frac{1}{2} m v^2$)")
        col1, col2 = st.columns(2)
        with col1:
            m = st.number_input("Mass (m) in kg", min_value=0.0, value=15.0, step=0.5)
        with col2:
            v = st.number_input("Velocity (v) in m/s", value=20.0, step=0.5)
        if st.button("Calculate Kinetic Energy"):
            ke = 0.5 * m * (v ** 2)
            st.success(f"Kinetic Energy ($KE$) = **{ke:.4f} J**")

# ================= 2. STRENGTH OF MATERIALS =================
elif module == "2. Strength of Materials":
    st.header("2. Strength of Materials")
    sub_calc = st.radio(
        "Choose Calculation:",
        ["Stress", "Strain", "Young's Modulus"],
        horizontal=True
    )

    if sub_calc == "Stress":
        st.subheader("Direct Stress ($\\sigma = F / A$)")
        col1, col2 = st.columns(2)
        with col1:
            f = st.number_input("Applied Load / Force (F) in N", value=10000.0, step=100.0)
        with col2:
            a = st.number_input("Cross-sectional Area (A) in m²", min_value=1e-8, value=0.002, format="%.6f")
        if st.button("Calculate Stress"):
            stress = f / a
            st.success(f"Stress ($\\sigma$) = **{stress:.2f} Pa** ({stress/1e6:.4f} MPa)")

    elif sub_calc == "Strain":
        st.subheader("Linear Strain ($\\varepsilon = \\Delta L / L$)")
        col1, col2 = st.columns(2)
        with col1:
            dl = st.number_input("Change in Length (ΔL) in mm", value=0.05, step=0.005, format="%.4f")
        with col2:
            l = st.number_input("Original Length (L) in mm", min_value=0.001, value=500.0, step=1.0)
        if st.button("Calculate Strain"):
            strain = dl / l
            st.success(f"Strain ($\\varepsilon$) = **{strain:.6e}** (Dimensionless)")

    elif sub_calc == "Young's Modulus":
        st.subheader("Young's Modulus of Elasticity ($E = \\sigma / \\varepsilon$)")
        col1, col2 = st.columns(2)
        with col1:
            stress = st.number_input("Stress (σ) in Pa", value=200000000.0, step=1e6)
        with col2:
            strain = st.number_input("Strain (ε)", min_value=1e-9, value=0.001, format="%.6f")
        if st.button("Calculate Young's Modulus"):
            e = stress / strain
            st.success(f"Young's Modulus ($E$) = **{e:.4e} Pa** ({e/1e9:.2f} GPa)")

# ================= 3. THERMODYNAMICS =================
elif module == "3. Thermodynamics":
    st.header("3. Thermodynamics")
    sub_calc = st.radio(
        "Choose Calculation:",
        ["Heat Transfer", "Work Done", "Thermal Efficiency"],
        horizontal=True
    )

    if sub_calc == "Heat Transfer":
        st.subheader("Sensible Heat Transfer ($Q = m \\times c_p \\times \\Delta T$)")
        col1, col2, col3 = st.columns(3)
        with col1:
            m = st.number_input("Mass (m) in kg", min_value=0.0, value=2.0, step=0.1)
        with col2:
            cp = st.number_input("Specific Heat ($c_p$) in J/kg·K", min_value=0.0, value=4184.0, step=10.0)
        with col3:
            dt = st.number_input("Temperature Difference (ΔT) in K or °C", value=25.0, step=1.0)
        if st.button("Calculate Heat Transfer"):
            q = m * cp * dt
            st.success(f"Heat Transfer ($Q$) = **{q:.2f} J** ({q/1000:.3f} kJ)")

    elif sub_calc == "Work Done":
        st.subheader("Boundary Work Done ($W = P \\times \\Delta V$)")
        col1, col2 = st.columns(2)
        with col1:
            p = st.number_input("Constant Pressure (P) in Pa", min_value=0.0, value=101325.0, step=500.0)
        with col2:
            dv = st.number_input("Change in Volume (ΔV) in m³", value=0.02, step=0.001, format="%.4f")
        if st.button("Calculate Work Done"):
            w = p * dv
            st.success(f"Work Done ($W$) = **{w:.2f} J** ({w/1000:.4f} kJ)")

    elif sub_calc == "Thermal Efficiency":
        st.subheader("Thermal Efficiency ($\\eta = W_{net} / Q_{in}$)")
        col1, col2 = st.columns(2)
        with col1:
            w_net = st.number_input("Net Work Done ($W_{net}$) in kJ", value=40.0, step=1.0)
        with col2:
            q_in = st.number_input("Heat Supplied ($Q_{in}$) in kJ", min_value=0.001, value=100.0, step=1.0)
        if st.button("Calculate Thermal Efficiency"):
            eta = (w_net / q_in) * 100
            st.success(f"Thermal Efficiency ($\\eta$) = **{eta:.2f} %**")

# ================= 4. FLUID MECHANICS =================
elif module == "4. Fluid Mechanics":
    st.header("4. Fluid Mechanics")
    sub_calc = st.radio(
        "Choose Calculation:",
        ["Pressure", "Reynolds Number", "Flow Velocity", "Discharge"],
        horizontal=True
    )

    if sub_calc == "Pressure":
        st.subheader("Fluid Pressure ($P = F / A$)")
        col1, col2 = st.columns(2)
        with col1:
            f = st.number_input("Normal Force (F) in N", value=500.0, step=10.0)
        with col2:
            a = st.number_input("Area (A) in m²", min_value=1e-8, value=0.05, format="%.4f")
        if st.button("Calculate Pressure"):
            p = f / a
            st.success(f"Pressure ($P$) = **{p:.2f} Pa** ({p/1000:.3f} kPa)")

    elif sub_calc == "Reynolds Number":
        st.subheader("Reynolds Number ($Re = \\frac{\\rho \\times v \\times D}{\\mu}$)")
        col1, col2 = st.columns(2)
        with col1:
            rho = st.number_input("Density (ρ) in kg/m³", min_value=0.001, value=1000.0, step=1.0)
            v = st.number_input("Velocity (v) in m/s", min_value=0.0, value=1.5, step=0.1)
        with col2:
            d = st.number_input("Diameter (D) in m", min_value=1e-6, value=0.05, format="%.4f")
            mu = st.number_input("Dynamic Viscosity (μ) in Pa·s", min_value=1e-7, value=0.001002, format="%.6f")
        if st.button("Calculate Reynolds Number"):
            re = (rho * v * d) / mu
            regime = "Laminar Flow (Re < 2300)" if re < 2300 else ("Transitional Flow (2300 ≤ Re ≤ 4000)" if re <= 4000 else "Turbulent Flow (Re > 4000)")
            st.success(f"Reynolds Number ($Re$) = **{re:.2f}**")
            st.info(f"Flow Regime: **{regime}**")

    elif sub_calc == "Flow Velocity":
        st.subheader("Flow Velocity ($v = Q / A$)")
        col1, col2 = st.columns(2)
        with col1:
            q = st.number_input("Discharge (Q) in m³/s", min_value=0.0, value=0.02, step=0.001, format="%.4f")
        with col2:
            a = st.number_input("Pipe Area (A) in m²", min_value=1e-8, value=0.005, format="%.6f")
        if st.button("Calculate Flow Velocity"):
            v = q / a
            st.success(f"Flow Velocity ($v$) = **{v:.4f} m/s**")

    elif sub_calc == "Discharge":
        st.subheader("Discharge ($Q = A \\times v$)")
        col1, col2 = st.columns(2)
        with col1:
            a = st.number_input("Pipe Area (A) in m²", min_value=0.0, value=0.005, format="%.6f")
        with col2:
            v = st.number_input("Velocity (v) in m/s", min_value=0.0, value=4.0, step=0.1)
        if st.button("Calculate Discharge"):
            q = a * v
            st.success(f"Discharge ($Q$) = **{q:.4f} m³/s** ({q * 1000:.2f} Liters/s)")

# ================= 5. THERMAL ENGINEERING =================
elif module == "5. Thermal Engineering":
    st.header("5. Thermal Engineering")
    sub_calc = st.radio(
        "Choose Calculation:",
        ["Heat Conduction", "COP", "Heat-Engine Efficiency"],
        horizontal=True
    )

    if sub_calc == "Heat Conduction":
        st.subheader("Fourier's Law of Heat Conduction ($Q = \\frac{k \\times A \\times \\Delta T}{L}$)")
        col1, col2 = st.columns(2)
        with col1:
            k = st.number_input("Thermal Conductivity (k) in W/m·K", min_value=0.0, value=45.0, step=0.5)
            a = st.number_input("Surface Area (A) in m²", min_value=0.001, value=1.5, step=0.1)
        with col2:
            dt = st.number_input("Temperature Difference (ΔT) in K or °C", value=80.0, step=1.0)
            dx = st.number_input("Thickness / Length (L) in meters", min_value=1e-5, value=0.02, step=0.005, format="%.4f")
        if st.button("Calculate Conduction Rate"):
            q_cond = (k * a * abs(dt)) / dx
            st.success(f"Rate of Heat Transfer ($Q$) = **{q_cond:.2f} W**")

    elif sub_calc == "COP":
        st.subheader("Coefficient of Performance (COP)")
        device = st.selectbox("Device Type", ["Refrigerator", "Heat Pump"])
        col1, col2 = st.columns(2)
        with col1:
            q_desired = st.number_input("Desired Heat Effect (kW or kJ)", min_value=0.0, value=3.5, step=0.1)
        with col2:
            w_in = st.number_input("Work Input ($W_{in}$) in kW or kJ", min_value=0.001, value=1.0, step=0.1)
        if st.button("Calculate COP"):
            cop = q_desired / w_in
            st.success(f"COP of {device} = **{cop:.3f}**")

    elif sub_calc == "Heat-Engine Efficiency":
        st.subheader("Carnot Heat Engine Efficiency ($\\eta = 1 - \\frac{T_L}{T_H}$)")
        col1, col2 = st.columns(2)
        with col1:
            th = st.number_input("Source Temperature ($T_H$) in Kelvin", min_value=1.0, value=800.0, step=10.0)
        with col2:
            tl = st.number_input("Sink Temperature ($T_L$) in Kelvin", min_value=1.0, value=300.0, step=10.0)
        if st.button("Calculate Carnot Efficiency"):
            if tl >= th:
                st.error("Sink Temperature (TL) must be strictly lower than Source Temperature (TH).")
            else:
                eta = (1 - (tl / th)) * 100
                st.success(f"Maximum Carnot Efficiency ($\\eta$) = **{eta:.2f} %**")

# ================= 6. MACHINE DESIGN =================
elif module == "6. Machine Design":
    st.header("6. Machine Design")
    sub_calc = st.radio(
        "Choose Calculation:",
        ["Torque", "Shaft Power", "Shaft Diameter"],
        horizontal=True
    )

    if sub_calc == "Torque":
        st.subheader("Torque from Power and RPM ($T = \\frac{P}{\\omega}$)")
        col1, col2 = st.columns(2)
        with col1:
            p = st.number_input("Power (P) in Watts", min_value=0.0, value=7500.0, step=100.0)
        with col2:
            n = st.number_input("Rotational Speed (N) in RPM", min_value=0.1, value=1440.0, step=10.0)
        if st.button("Calculate Torque"):
            omega = (2 * math.pi * n) / 60
            torque = p / omega
            st.success(f"Torque ($T$) = **{torque:.4f} N·m**")

    elif sub_calc == "Shaft Power":
        st.subheader("Shaft Power ($P = \\frac{2\\pi N T}{60}$)")
        col1, col2 = st.columns(2)
        with col1:
            torque = st.number_input("Torque (T) in N·m", min_value=0.0, value=50.0, step=1.0)
        with col2:
            n = st.number_input("Rotational Speed (N) in RPM", min_value=0.0, value=1440.0, step=10.0)
        if st.button("Calculate Shaft Power"):
            power = (2 * math.pi * n * torque) / 60
            st.success(f"Power ($P$) = **{power:.2f} W** ({power/1000:.3f} kW)")

    elif sub_calc == "Shaft Diameter":
        st.subheader("Solid Shaft Diameter (Torsion Formula)")
        st.latex(r"d = \left( \frac{16 T}{\pi \tau} \right)^{1/3}")
        col1, col2 = st.columns(2)
        with col1:
            torque = st.number_input("Applied Torque (T) in N·m", min_value=0.0, value=250.0, step=10.0)
        with col2:
            tau = st.number_input("Permissible Shear Stress (τ) in MPa", min_value=0.1, value=40.0, step=1.0)
        if st.button("Calculate Shaft Diameter"):
            tau_pa = tau * 1e6
            d = ((16 * torque) / (math.pi * tau_pa)) ** (1 / 3)
            d_mm = d * 1000
            st.success(f"Minimum Shaft Diameter ($d$) = **{d_mm:.2f} mm** ({d:.5f} m)")