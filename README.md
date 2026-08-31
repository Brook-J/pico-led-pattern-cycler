# pico-led-pattern-cycler
 A <mark>Raspberry Pi Pico</mark> Embedded Systems project which uses 4 LEDs to create and cycle through 4 LED patterns with a button.


 ## 💻 Software Features (`Micro Python`)
 **utilizes:**
* Uses SubPrograms (Functions (`def`) to output and store the various LED patterns onto the LEDs.
* Utilizes Blocking functions (`time.sleep`) to create the pattern combinations.
* Utilizes Polling Mechanisms to detect button presses via an `if/elif` statement within an infinite while `True loop`.

## ⚙️ Components list:
  * Raspberry Pi Pico microcontroller
  * 1x Button
  * 4x LEDs (Red, Green, Blue, Yellow)
  * 4 Resistors (120PCS +)
  * 7x Jumper wires

## 📟 How to setup components.
 * **GPIO Pin connection**
   * Red LED - `GP17`
   * Green LED - `GP16`
   * Blue LED - `GP14`
   * Yellow LED - `GP15`
  
   * Button - `GP13`
   
     <img width="319" height="369" alt="image" src="https://github.com/user-attachments/assets/c113f367-3729-4a5a-90d4-9178bbbec623" />


1. **Ground (GND) Common Rail:** Connect a physical `GND` pin from the Raspberry Pi Pico to the Ground Rail on the breadboard (marked by the blue row). This serves as the common ground path returning the negative current for all components.

2. **LED Orientations & Wiring:**
   * Plug the shorter leg (**Cathode / Negative**) of each LED directly into the Ground rail.
   * Plug the longer leg (**Anode / Positive**) into a separate row on the breadboard's terminal strips.

3. **Resistors & Control Lines:**
   * Connect one side of a current-limiting resistor to the positive leg of each LED via the breadboard terminal strip.
   * Bridge the other side of the resistor across the center ravine using jumper wires running back to the designated `GP` pins. Ensure all assignments match the pin mapping table precisely.

4. **Button Wiring**
    * Mount the push button directly across the central ravine (the plastic divider gap) of the breadboard.
    * Connect one side of the button to `GP13` via a jumper wire. Connect the opposite pin directly to the Ground rail (`GND`)
      - Ensure the two jumper wires (running to `GP13` and `GND`) are connected **diagonally** from each other across the switch corners.


## 🔌 Circuit Diagram

<img width="546" height="174" alt="image" src="https://github.com/user-attachments/assets/3917f19d-a33f-466a-b37b-0e95996a7aab" />


## 🚀 How to Run the Code in Thonny IDE

Follow these steps to run the MicroPython script onto your Raspberry Pi Pico:

1. **Install Thonny IDE:** Download and install the software from [thonny.org](https://thonny.org).
2. **Connect the Microcontroller:** Connect your Raspberry Pi Pico to your computer using a micro-USB cable.
3. **Configure the Interpreter:**
   * Open Thonny.
   * Look at the bottom-right corner of the window and click on the language profile text.
   * Select **Configure interpreter...**
   * Under the *Interpreter* tab, select **MicroPython (Raspberry Pi Pico)** from the dropdown menu and click **OK**.
4. **Load the Project:**
   * Create a new file in Thonny.
   * Copy the MicroPython script from this repository and paste it into the empty editor window.
5. **Save to the Pico:**
   * Click **File > Save As...**
   * Thonny will ask where you want to save the code. Select **Raspberry Pi Pico**.
   * Name the file exactly `main.py` and click **Save**. *(Naming it `main.py` tells the Pico to run this script automatically whenever it receives power).*
6. **Execute:** Click the green **Run Current Script** button (or press `F5`) in the top toolbar to start cycling through the LED patterns!







 


