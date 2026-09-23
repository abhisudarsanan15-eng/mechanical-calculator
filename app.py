import math
import sys

# ----------------- Visual Styling & Colors -----------------
class Style:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    
    # Colors
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    MAGENTA = "\033[95m"
    BLUE = "\033[94m"

def print_result_box(title, value_str, formula_str):
    """Prints a styled decorative box for computed final answers."""
    content_lines = [
        f"  Module / Property : {Style.BOLD}{title}{Style.RESET}",
        f"  Governing Formula : {Style.CYAN}{formula_str}{Style.RESET}",
        f"  Computed Result   : {Style.GREEN}{Style.BOLD}{Style.UNDERLINE}{value_str}{Style.RESET}"
    ]
    # Strip ANSI sequences to calculate border length
    raw_lengths = [len(f"  Module / Property : {title}"),
                   len(f"  Governing Formula : {formula_str}"),
                   len(f"  Computed Result   : {value_str}")]
    box_width = max(max(raw_lengths) + 4, 48)
    
    print("\n" + Style.YELLOW + "╔" + "═" * box_width + "╗" + Style.RESET)
    for i, line in enumerate(content_lines):
        pad = box_width - raw_lengths[i]
        print(Style.YELLOW + "║" + Style.RESET + line + " " * pad + Style.YELLOW + "║" + Style.RESET)
    print(Style.YELLOW + "╚" + "═" * box_width + "╝" + Style.RESET + "\n")

# ----------------- Input Helper Functions -----------------
def get_positive_float(prompt_text):
    """Formatted input validator for positive numerical values."""
    formatted_prompt = f" {Style.CYAN}➤{Style.RESET} {Style.BOLD}{prompt_text}{Style.RESET}: "
    while True:
        try:
            val = float(input(formatted_prompt))
            if val < 0:
                print(f"   {Style.RED}✖ Error: Value cannot be negative. Please try again.{Style.RESET}")
                continue
            return val
        except ValueError:
            print(f"   {Style.RED}✖ Error: Invalid input! Please enter a valid real number.{Style.RESET}")

def get_nonzero_float(prompt_text):
    """Formatted input validator for non-zero values (denominators)."""
    while True:
        val = get_positive_float(prompt_text)
        if val == 0:
            print(f"   {Style.RED}✖ Error: Value cannot be zero. Please try again.{Style.RESET}")
            continue
        return val


# ================= 1. Mechanics =================
def calc_force():
    m = get_positive_float("Enter mass (kg)")
    a = get_positive_float("Enter acceleration (m/s²)")
    ans = f"{m * a:.4f} N"
    print_result_box("Mechanics - Force", ans, "F = m * a")

def calc_work():
    f = get_positive_float("Enter force (N)")
    d = get_positive_float("Enter displacement (m)")
    ans = f"{f * d:.4f} J"
    print_result_box("Mechanics - Work Done", ans, "W = F * d")

def calc_power():
    w = get_positive_float("Enter work done (J)")
    t = get_nonzero_float("Enter time (s)")
    ans = f"{w / t:.4f} W"
    print_result_box("Mechanics - Power", ans, "P = W / t")

def calc_kinetic_energy():
    m = get_positive_float("Enter mass (kg)")
    v = get_positive_float("Enter velocity (m/s)")
    ans = f"{0.5 * m * (v ** 2):.4f} J"
    print_result_box("Mechanics - Kinetic Energy", ans, "KE = 0.5 * m * v²")

def menu_mechanics():
    while True:
        print(f"\n{Style.BLUE}──────── 1. MECHANICS ────────{Style.RESET}")
        print(" [1] Force")
        print(" [2] Work")
        print(" [3] Power")
        print(" [4] Kinetic Energy")
        print(" [5] Return to Main Menu")
        choice = input(f" {Style.YELLOW}Select option (1-5):{Style.RESET} ").strip()
        
        if choice == '1': calc_force()
        elif choice == '2': calc_work()
        elif choice == '3': calc_power()
        elif choice == '4': calc_kinetic_energy()
        elif choice == '5': break
        else: print(f" {Style.RED}Invalid option! Choose between 1 and 5.{Style.RESET}")


# ================= 2. Strength of Materials =================
def calc_stress():
    f = get_positive_float("Enter axial load/force (N)")
    a = get_nonzero_float("Enter cross-sectional area (m²)")
    ans = f"{f / a:.4f} Pa (N/m²)"
    print_result_box("SOM - Direct Stress", ans, "σ = F / A")

def calc_strain():
    dl = get_positive_float("Enter elongation/deformation ΔL (m)")
    l = get_nonzero_float("Enter original length L (m)")
    ans = f"{dl / l:.6f} (dimensionless)"
    print_result_box("SOM - Longitudinal Strain", ans, "ε = ΔL / L")

def calc_youngs_modulus():
    stress = get_positive_float("Enter stress σ (Pa)")
    strain = get_nonzero_float("Enter strain ε")
    ans = f"{stress / strain:.4f} Pa"
    print_result_box("SOM - Young's Modulus", ans, "E = σ / ε")

def menu_som():
    while True:
        print(f"\n{Style.BLUE}──── 2. STRENGTH OF MATERIALS ────{Style.RESET}")
        print(" [1] Stress")
        print(" [2] Strain")
        print(" [3] Young's Modulus")
        print(" [4] Return to Main Menu")
        choice = input(f" {Style.YELLOW}Select option (1-4):{Style.RESET} ").strip()
        
        if choice == '1': calc_stress()
        elif choice == '2': calc_strain()
        elif choice == '3': calc_youngs_modulus()
        elif choice == '4': break
        else: print(f" {Style.RED}Invalid option! Choose between 1 and 4.{Style.RESET}")


# ================= 3. Thermodynamics =================
def calc_heat_transfer():
    m = get_positive_float("Enter mass (kg)")
    c = get_positive_float("Enter specific heat capacity (J/kg·K)")
    formatted_prompt = f" {Style.CYAN}➤{Style.RESET} {Style.BOLD}Enter temperature change ΔT (K or °C){Style.RESET}: "
    dt = float(input(formatted_prompt))
    ans = f"{m * c * dt:.4f} J"
    print_result_box("Thermodynamics - Heat Transfer", ans, "Q = m * c * ΔT")

def calc_thermo_work():
    p = get_positive_float("Enter constant pressure P (Pa)")
    formatted_prompt = f" {Style.CYAN}➤{Style.RESET} {Style.BOLD}Enter change in volume ΔV (m³){Style.RESET}: "
    dv = float(input(formatted_prompt))
    ans = f"{p * dv:.4f} J"
    print_result_box("Thermodynamics - Boundary Work", ans, "W = P * ΔV")

def calc_thermal_efficiency():
    w = get_positive_float("Enter net work output W (J)")
    qin = get_nonzero_float("Enter heat input Qin (J)")
    if w > qin:
        print(f"   {Style.RED}✖ Error: Work output cannot exceed heat input.{Style.RESET}")
        return
    ans = f"{(w / qin) * 100:.2f} %"
    print_result_box("Thermodynamics - Efficiency", ans, "η = (W / Qin) * 100")

def menu_thermo():
    while True:
        print(f"\n{Style.BLUE}────── 3. THERMODYNAMICS ──────{Style.RESET}")
        print(" [1] Heat Transfer")
        print(" [2] Work Done")
        print(" [3] Thermal Efficiency")
        print(" [4] Return to Main Menu")
        choice = input(f" {Style.YELLOW}Select option (1-4):{Style.RESET} ").strip()
        
        if choice == '1': calc_heat_transfer()
        elif choice == '2': calc_thermo_work()
        elif choice == '3': calc_thermal_efficiency()
        elif choice == '4': break
        else: print(f" {Style.RED}Invalid option! Choose between 1 and 4.{Style.RESET}")


# ================= 4. Fluid Mechanics =================
def calc_pressure():
    rho = get_positive_float("Enter fluid density ρ (kg/m³)")
    h = get_positive_float("Enter column height/depth h (m)")
    ans = f"{rho * 9.81 * h:.4f} Pa"
    print_result_box("Fluid Mechanics - Hydrostatic Pressure", ans, "P = ρ * g * h (g = 9.81 m/s²)")

def calc_reynolds_number():
    rho = get_positive_float("Enter fluid density ρ (kg/m³)")
    v = get_positive_float("Enter flow velocity v (m/s)")
    d = get_positive_float("Enter pipe diameter D (m)")
    mu = get_nonzero_float("Enter dynamic viscosity μ (Pa·s)")
    ans = f"{(rho * v * d) / mu:.2f} (dimensionless)"
    print_result_box("Fluid Mechanics - Reynolds Number", ans, "Re = (ρ * v * D) / μ")

def calc_flow_velocity():
    q = get_positive_float("Enter discharge Q (m³/s)")
    a = get_nonzero_float("Enter pipe cross-section area A (m²)")
    ans = f"{q / a:.4f} m/s"
    print_result_box("Fluid Mechanics - Flow Velocity", ans, "v = Q / A")

def calc_discharge():
    a = get_positive_float("Enter flow area A (m²)")
    v = get_positive_float("Enter velocity v (m/s)")
    ans = f"{a * v:.4f} m³/s"
    print_result_box("Fluid Mechanics - Volumetric Discharge", ans, "Q = A * v")

def menu_fluids():
    while True:
        print(f"\n{Style.BLUE}───── 4. FLUID MECHANICS ─────{Style.RESET}")
        print(" [1] Hydrostatic Pressure")
        print(" [2] Reynolds Number")
        print(" [3] Flow Velocity")
        print(" [4] Volumetric Discharge")
        print(" [5] Return to Main Menu")
        choice = input(f" {Style.YELLOW}Select option (1-5):{Style.RESET} ").strip()
        
        if choice == '1': calc_pressure()
        elif choice == '2': calc_reynolds_number()
        elif choice == '3': calc_flow_velocity()
        elif choice == '4': calc_discharge()
        elif choice == '5': break
        else: print(f" {Style.RED}Invalid option! Choose between 1 and 5.{Style.RESET}")


# ================= 5. Thermal Engineering =================
def calc_heat_conduction():
    k = get_positive_float("Enter thermal conductivity k (W/m·K)")
    a = get_positive_float("Enter surface area A (m²)")
    formatted_prompt = f" {Style.CYAN}➤{Style.RESET} {Style.BOLD}Enter temperature difference ΔT (K or °C){Style.RESET}: "
    dt = float(input(formatted_prompt))
    dx = get_nonzero_float("Enter wall thickness dx (m)")
    ans = f"{(k * a * abs(dt)) / dx:.4f} W"
    print_result_box("Thermal Engg - Heat Conduction", ans, "Q = (k * A * ΔT) / dx")

def calc_cop():
    q_effect = get_positive_float("Enter desired cooling/heating effect (W or J)")
    w_in = get_nonzero_float("Enter net work input W (W or J)")
    ans = f"{q_effect / w_in:.4f}"
    print_result_box("Thermal Engg - COP", ans, "COP = Q_effect / W_in")

def calc_heat_engine_eff():
    th = get_positive_float("Enter hot reservoir temperature TH (K)")
    tl = get_positive_float("Enter cold reservoir temperature TL (K)")
    if tl >= th:
        print(f"   {Style.RED}✖ Error: TL must be lower than TH.{Style.RESET}")
        return
    ans = f"{(1 - (tl / th)) * 100:.2f} %"
    print_result_box("Thermal Engg - Carnot Engine Efficiency", ans, "η = (1 - TL/TH) * 100")

def menu_thermal_eng():
    while True:
        print(f"\n{Style.BLUE}──── 5. THERMAL ENGINEERING ────{Style.RESET}")
        print(" [1] Heat Conduction")
        print(" [2] Coefficient of Performance (COP)")
        print(" [3] Heat-Engine Efficiency")
        print(" [4] Return to Main Menu")
        choice = input(f" {Style.YELLOW}Select option (1-4):{Style.RESET} ").strip()
        
        if choice == '1': calc_heat_conduction()
        elif choice == '2': calc_cop()
        elif choice == '3': calc_heat_engine_eff()
        elif choice == '4': break
        else: print(f" {Style.RED}Invalid option! Choose between 1 and 4.{Style.RESET}")


# ================= 6. Machine Design =================
def calc_torque():
    p = get_positive_float("Enter power transmitted P (W)")
    n = get_nonzero_float("Enter shaft rotational speed N (RPM)")
    t = (60 * p) / (2 * math.pi * n)
    ans = f"{t:.4f} N·m"
    print_result_box("Machine Design - Torque", ans, "T = (60 * P) / (2 * π * N)")

def calc_shaft_power():
    t = get_positive_float("Enter torque T (N·m)")
    n = get_positive_float("Enter shaft rotational speed N (RPM)")
    power = (2 * math.pi * n * t) / 60
    ans = f"{power:.4f} W ({power/1000:.4f} kW)"
    print_result_box("Machine Design - Shaft Power", ans, "P = (2 * π * N * T) / 60")

def calc_shaft_diameter():
    t = get_positive_float("Enter applied torque T (N·m)")
    tau = get_nonzero_float("Enter allowable shear stress τ (Pa)")
    d = ((16 * t) / (math.pi * tau)) ** (1 / 3)
    ans = f"{d:.4f} m  ({d * 1000:.2f} mm)"
    print_result_box("Machine Design - Shaft Diameter", ans, "d = [(16 * T) / (π * τ)]^(1/3)")

def menu_machine_design():
    while True:
        print(f"\n{Style.BLUE}────── 6. MACHINE DESIGN ──────{Style.RESET}")
        print(" [1] Torque")
        print(" [2] Shaft Power")
        print(" [3] Solid Shaft Diameter")
        print(" [4] Return to Main Menu")
        choice = input(f" {Style.YELLOW}Select option (1-4):{Style.RESET} ").strip()
        
        if choice == '1': calc_torque()
        elif choice == '2': calc_shaft_power()
        elif choice == '3': calc_shaft_diameter()
        elif choice == '4': break
        else: print(f" {Style.RED}Invalid option! Choose between 1 and 4.{Style.RESET}")


# ================= Main Controller Loop =================
def main():
    while True:
        print(f"\n{Style.MAGENTA}{Style.BOLD}" + "═" * 50)
        print("       MECHANICAL ENGINEERING CALCULATOR")
        print("═" * 50 + f"{Style.RESET}")
        print(f"{Style.CYAN} 1.{Style.RESET} Mechanics")
        print(f"{Style.CYAN} 2.{Style.RESET} Strength of Materials")
        print(f"{Style.CYAN} 3.{Style.RESET} Thermodynamics")
        print(f"{Style.CYAN} 4.{Style.RESET} Fluid Mechanics")
        print(f"{Style.CYAN} 5.{Style.RESET} Thermal Engineering")
        print(f"{Style.CYAN} 6.{Style.RESET} Machine Design")
        print(f"{Style.RED} 7. Exit{Style.RESET}")
        print(f"{Style.MAGENTA}" + "─" * 50 + f"{Style.RESET}")
        
        choice = input(f" {Style.YELLOW}Select Module (1-7):{Style.RESET} ").strip()
        
        if choice == '1': menu_mechanics()
        elif choice == '2': menu_som()
        elif choice == '3': menu_thermo()
        elif choice == '4': menu_fluids()
        elif choice == '5': menu_thermal_eng()
        elif choice == '6': menu_machine_design()
        elif choice == '7':
            print(f"\n{Style.GREEN}✔ Exiting calculator. Have a great day!{Style.RESET}\n")
            break
        else:
            print(f" {Style.RED}✖ Invalid selection! Please enter a number from 1 to 7.{Style.RESET}")

if __name__ == "__main__":
    main()
