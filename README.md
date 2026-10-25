# musicDevice
A small MIDI capable keypad powered by an esp32-s3 for native USB compatibility

<img width="555" height="371" alt="Screenshot 2026-10-25 173044" src="https://github.com/user-attachments/assets/5828e6e9-7e5c-4425-8be3-18b6c7b702eb" />


Components
- EC11 Rotary encoder
- SK6812 MINI-E neopixels
- Bourns Slide Potentiometers
- Kailh Choc Low-Profile Switches

The midi keys are built to be activated by capacitive touch based on the exposed copper on the PCB

I built this since I don't have a lot of space for an entire keyboard, so something simple can hopefully allow me to get something ready quickly if necessary
The lights on the back should also add a nice touch and some element of customizability

<img width="389" height="356" alt="pcb back Screenshot 2026-10-24 101311" src="https://github.com/user-attachments/assets/3d34d932-b2f9-44b4-95b4-2954b8a09a07" />



### Usage

Use [kmk firmware](https://github.com/KMKfw/kmk_firmware/tree/main) to get a circuitpython environment for the device to use the mechanical keyboard

MIDI configuration is dependent on the user's configuration

### 3D Casing
Included in the `\3dModels\` directory are another two directories, one (`\editable\`) with the original editable kicad file for the enclosure. The other (`\printable\`) is where print ready 3mf files for the case are provided

<img width="833" height="500" alt="Screenshot 2026-10-25 184453" src="https://github.com/user-attachments/assets/af30f714-0aff-44b3-af97-6220086148f7" />


### Bill of Materials

| Ref     | Qty | Suggested Component             | Purpose | Supplier                                                   |
|---------|---|---------------------------------|-----------------------------------------------------------| -- |
| D1-D3   | 3 | SK6812 mini-e                   | Addressable LEDs behind keycaps| [JLCPCB](https://jlcpcb.com/partdetail/SK6812MINI-E/C5149201)  [Aliexpress](https://www.aliexpress.com/item/1005005193716172.html)                         |
| RV1-RV2 | 2 | Bourns PTA1543                  | Sliding potentiometer| [Mouser](https://www.mouser.ca/en/ProductDetail/Bourns/PTA1543-2015CIA103) [Aliexpress](https://www.aliexpress.com/item/1005003684684538.html)                                     |
| SW1-SW3 | 3 | Kailh Choc Low-Profile Switches | Nice mechanical keys| [Aliexpress](https://www.aliexpress.com/item/1005006120461718.html)                                      |
| SW4     | 1 | EC11 Rotary Encoder | knob             | [Aliexpress](https://www.aliexpress.com/item/1005007644083514.html) -- I Possess                                                      |
| U1      | 1 | Waveshare ESP32-S3-Zero         | Small form factor esp32, and is natively supported by KMK | [Aliexpress](https://www.aliexpress.com/item/1005012733231291.html)


### References
Based on the tutorial created by [KaiPerira](https://github.com/KaiPereira/midi-keypad)

