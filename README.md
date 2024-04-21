<h1 align = "center">
	Superfarm 4.0 Hypixel Farming Helper
</h1>

`hypixel-farming-helper` is small helper for using the [Superfarm 4.0](https://www.youtube.com/watch?v=9g3YTqrVgC4). It
intercepts global key presses and provides a helpful "sticky key" experience. Works best with
the [SkyHanni](https://github.com/hannibal002/SkyHanni) mod.

Tested on MacOS Sonoma. Compiling process only supports MacOS for now.

## Prerequisites

- [Python 3.x](https://www.python.org/downloads/)
- [SkyHanni](https://github.com/hannibal002/SkyHanni) (optional - if not used will need to bind X to break blocks in
  game controls)

## Installation

Follow these steps to get your Hypixel Farming Helper up and running:

### Step 1: Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/superfarm-hypixel.git
cd superfarm-hypixel
```

### Step 2: Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install all necessary dependencies by running:

```bash
pip install -r requirements.txt
```

### Step 4: Build the Application (MacOS only)

Build the application using the setup script:

```bash
python3 setup.py py2app
```

### Step 5: Run the Application (MacOS only)

Navigate to the `/dist` folder and run the compiled application, or run from Terminal:

```bash
open -a Hypixel\ Farming\ Helper.app
```

You should be prompted with "input monitoring permissions required". Navigate to System Settings > Privacy > Input
Monitoring, and turn them on there.

You may need to add Accessibility permissions as well (Privacy > Accessibility)

### Running the Application on Windows

Run the app using python directly:

```bash
python3 app.py
```

## Usage

To use the Hypixel Farming Helper, select a mode (Melon, Cocoa Beans, etc...), and press start. The application will
intercept global keyboard events, and allow you to have a **sticky key** experience while farming. The keys line up with
the instructions found on the [Superfarm 4.0 Guide](https://www.youtube.com/watch?v=eggg747eG2Y)

The helper intercepts all four **arrow keys**, and the **right shift key**. The right shift key releases all held keys,
and the arrow keys do the following depending on the selected mode:

### Melon / Pumpkin

- Left: Break and move left - x and a
- Right: Break and move right - x and d
- Up: Move forwards - w
- Down: Move backwards - s

### Cocoa Beans

- Left: Move left - a
- Right: Move right - d
- Up: Break and move forwards - x and w
- Down: Break and move backwards - x and s

### Mushroom

- Left: Break and move forward-left - x, w, and a
- Right: Break and move right - x and d
- Up: Move forwards - w
- Down: Move backwards - s

### Sugarcane

- Left: Break and move left - x and a
- Right: Break and move backwards - x and s
- Up: Move forwards - w
- Down: Move backwards - s

### Cactus

- Left: Break and move left - x and a
- Right: Break and move right - x and d
- Up: Move forwards - w
- Down: Move backwards - s

## Contributing

We welcome contributions to the Superfarm 4.0 Hypixel Farming Helper. Please feel free to fork the repository, make
changes, and submit pull requests. **Windows support please**

## License

This project is licensed under the MIT License - see the LICENSE file for details.