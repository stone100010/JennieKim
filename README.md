# JennieKim Christmas 3D Photo Gallery

An immersive 3D Christmas tree photo gallery showcasing Jennie Kim's photo collection with gesture control interactions.

## 🎄 Features

- **3D Christmas Tree Display**: Photos displayed as ornaments on a 3D Christmas tree
- **Gesture Control**: MediaPipe-powered hand gesture recognition for interaction
- **Dynamic Particle Effects**: Gold, green, red decorative balls and candy canes
- **Random Photo Browsing**: Smart random photo navigation without repetition
- **High-Quality Rendering**: UnrealBloom post-processing effects
- **Responsive Design**: Adapts to various screen sizes
- **Offline Operation**: Fully localized with no CDN dependencies

## 📁 Project Structure

```
Merry Christmas/
├── index.html              # Main application page
├── README.md               # Project documentation (English)
├── README_CN.md            # 项目说明文档 (Chinese)
├── assets/                 # Resource folder
│   ├── js/
│   │   └── photoGallery.js # Photo gallery management
│   ├── models/             # MediaPipe model files
│   │   └── hand_landmarker.task
│   └── wasm/               # WebAssembly files
│       ├── vision_wasm_internal.js
│       └── vision_wasm_internal.wasm
├── JennieKim/              # Original photo folder
└── JennieKim_430px/        # Processed photos (430px height)
```

## 🚀 Quick Start

### Local Development

1. Clone the repository
```bash
git clone https://github.com/stone100010/JennieKim.git
cd "Merry Christmas"
```

2. Start a local server
```bash
# Using Python
python -m http.server 8000

# Using Node.js
npx serve .

# Using PHP
php -S localhost:8000
```

3. Open `http://localhost:8000` in your browser

## 🎮 Interaction Controls

### Hand Gestures (Camera Required)
- **✊ Fist**: Switch to tree formation mode
- **✋ Open Palm**: Switch to scatter mode  
- **🤏 Pinch**: Focus on a random photo

### Debug Keyboard Shortcuts
- **R**: Reset photo browsing sequence
- **M**: Toggle between random/sequential browsing modes
- **P**: Show browsing progress in console

## 🛠️ Technical Stack

- **Three.js**: 3D graphics rendering
- **MediaPipe**: Hand gesture recognition
- **WebGL**: Hardware-accelerated rendering
- **Post-processing**: Bloom effects and tone mapping
- **WebAssembly**: MediaPipe local processing

## 📸 Photo Management

The project includes 260+ optimized Jennie Kim photos:

- **Format**: WebP
- **Dimensions**: Height 430px, aspect ratio preserved
- **Total Count**: 260+ photos
- **Location**: `JennieKim_430px/`

Photos are managed through the `photoGallery.js` module:
- Random photo selection
- Shuffle functionality
- Duplicate prevention
- Progress tracking

## 🎨 Visual Features

- **Particle System**: 1500 decorative particles + 2500 dust particles
- **Lighting System**: Multiple light sources including ambient, point, and spot lights
- **Material Effects**: Metallic finishes, glow effects, transparency
- **Post-processing**: Bloom effects, tone mapping
- **Real Aspect Ratio**: Photos maintain original proportions

## ⚙️ Configuration

Main configuration in the `CONFIG` object:

```javascript
const CONFIG = {
    colors: {
        bg: 0x000000,           // Background color
        champagneGold: 0xffd966, // Champagne gold
        deepGreen: 0x03180a,     // Deep green
        accentRed: 0x990000,     // Accent red
    },
    particles: {
        count: 1500,     // Decorative particles
        dustCount: 2500, // Dust particles
        treeHeight: 24,  // Tree height
        treeRadius: 8    // Tree radius
    }
};
```

## 🌟 Key Features

1. **Smart Photo Layout**: Automatic 3D space adaptation with correct aspect ratios
2. **Smooth Animations**: Optimized transitions for 60fps performance
3. **Real-time Gesture Detection**: Live hand tracking with multiple interaction modes
4. **Dynamic Loading**: Asynchronous photo loading without blocking
5. **Responsive Design**: Automatic adaptation to different devices and screens
6. **Random Browsing**: Intelligent random photo selection without repetition

## 📱 Browser Compatibility

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

### Requirements:
- WebGL 2.0
- ES6 Modules
- MediaPipe WebAssembly
- getUserMedia API
- Secure context (HTTPS or localhost)

## 🔧 Performance Optimizations

- **Local MediaPipe**: All models and WASM files localized for faster loading
- **Efficient Particle System**: Optimized rendering for smooth performance
- **Smart Photo Management**: Memory-efficient texture loading
- **Gesture Recognition**: GPU-accelerated hand tracking

## 🎯 Production Ready

This version is optimized for client deployment:
- Clean, minimal UI focused on photo display
- No upload functionality or user controls
- Default random browsing for engaging experience
- Fully offline operation

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## 🎁 Acknowledgments

- Three.js team for the excellent 3D library
- Google MediaPipe for gesture recognition technology
- All photo content creators

---

**Merry Christmas & Happy New Year! 🎄✨**