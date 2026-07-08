# Elite-driven-grey-wolf-optimization (EDGWO)
![Paper](https://img.shields.io/badge/Paper-ScienceDirect-red)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![NumPy](https://img.shields.io/badge/numpy-%3E%3D1.21.0-%23013243.svg?style=flat&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/matplotlib-%3E%3D3.3.0-%2311557c.svg?style=flat)
![Opfunu](https://img.shields.io/badge/opfunu-%3E%3D1.0.0-%234B8BBE.svg?style=flat)


## Introduction
這個專案實作了 `EDGWO` 的演算法內容以及進行了論文內容與其他演算法的比較，並且嘗試優化 `EDGWO`，我針對演算法容易陷入局部最佳解以及參數適應性不足的問題，提出了 `EDGWO_Kao` 版本，進一步提升了全局探索與區域開發的平衡能力。

如果你想了解完整的 EDGWO 演算法核心理論、數學公式推導與論文詳細介紹，請參考我寫的 [論文與演算法介紹](PAPER_INTRO.md)。

## Repository structure
本專案的目錄結構如下，主要分為演算法實作、歷史紀錄與繪圖輸出：
```text
├── algorithm/            # 存放各種最佳化演算法的 Python 實作
│   ├── EDGWO.py          # 基礎 EDGWO 演算法
│   ├── EDGWO_Kao.py      # 本專案改良版 EDGWO 演算法
│   ├── Gwo.py          
│   ├── PSO.py          
│   └── ... (包含 BES, cHGWOSCA, CHoA, HHO, MSGWO, REEGWO, SCSO 等)
├── assest/               # 論文比較照片儲存位置
├── history/              # 實驗紀錄與歷史數據儲存位置
├── photo/                # 實驗結果收斂圖表匯出資料夾
│   ├── 10_dim/           # 10 維度測試結果圖表
│   └── 20_dim/           # 20 維度測試結果圖表
├── main.py               # 實驗執行主程式
├── setting.py            # 實驗參數設定檔
├── requirement.txt       # 專案相依套件清單
├── README.md            
└── PAPER_INTRO.md        # 論文演算法詳細介紹
```

## Features
* **多種演算法實作**：除了 EDGWO 外，同時整合了十多種常見與先進的元啟發式演算法以利橫向比較。
* **標準測試集驗證**：支援 CEC2021 與 CEC2022 標準測試函數集(10/20 維度)，提供具公信力的實驗結果。

## Usage
可以按照以下方式執行程式 :
```bash
# 1. 複製專案
git clone https://github.com/KaoBraBra/edgwo-python.git
cd edgwo-python

# 2. 安裝套件
pip install -r requirement.txt

# 3. 執行程式 (可以先透過 setting 調整參數)
python main.py
```
以下為 setting 內容 :
```bash
dim = 20            # 維度
num_particles = 30  # 狼的總數
max_iter = 500      # 最多循環次數
UB = 100            # 上界
LB = -100           # 下界
Shift_Val = 20      # 函數的偏移量
exe_Val = 30        # 執行的次數
```

## Experimental Results
以下為論文中的比對項目，包括 CEC 2021 以及 CEC 2022。
### 1. CEC2021 In 10-Dimension
|Type|我實作的 EDGWO|論文中實作的 EDGWO|
|:-:|:-:|:-:|
|F3|![F3](photo/10_dim/CEC2021_F3.png)|![F3](assest/2021_10dim_f3.png)|
|F6|![F6](photo/10_dim/CEC2021_F6.png)|![F6](assest/2021_10dim_f6.png)|
|F8|![F8](photo/10_dim/CEC2021_F8.png)|![F8](assest/2021_10dim_f8.png)|
|F11|![F10](photo/10_dim/CEC2021_F10.png)|![F10](assest/2021_10dim_f10.png)|

### 2. CEC2021 In 20-Dimension
|Type|我實作的 EDGWO|論文中實作的 EDGWO|
|:-:|:-:|:-:|
|F4|![F4](photo/20_dim/CEC2021_F4.png)|![F4](assest/2021_20dim_f4.png)|
|F7|![F7](photo/20_dim/CEC2021_F7.png)|![F7](assest/2021_20dim_f7.png)|
|F8|![F8](photo/20_dim/CEC2021_F8.png)|![F8](assest/2021_20dim_f8.png)|
|F9|![F9](photo/20_dim/CEC2021_F9.png)|![F9](assest/2021_20dim_f9.png)|

### 3. CEC2022 In 10-Dimension
|Type|我實作的 EDGWO|論文中實作的 EDGWO|
|:-:|:-:|:-:|
|F2|![F2](photo/10_dim/CEC2022_F2.png)|![F2](assest/2022_10dim_f2.png)|
|F6|![F6](photo/10_dim/CEC2022_F6.png)|![F6](assest/2022_10dim_f6.png)|
|F8|![F8](photo/10_dim/CEC2022_F8.png)|![F8](assest/2022_10dim_f8.png)|
|F12|![F12](photo/10_dim/CEC2022_F12.png)|![F12](assest/2022_10dim_f12.png)|

### 4. CEC2022 In 20-Dimension
|Type|我實作的 EDGWO|論文中實作的 EDGWO|
|:-:|:-:|:-:|
|F7|![F7](photo/20_dim/CEC2022_F7.png)|![F7](assest/2022_20dim_f7.png)|
|F9|![F9](photo/20_dim/CEC2022_F9.png)|![F9](assest/2022_20dim_f9.png)|
|F10|![F10](photo/20_dim/CEC2022_F10.png)|![F10](assest/2022_20dim_f10.png)|
|F11|![F11](photo/20_dim/CEC2022_F11.png)|![F11](assest/2022_20dim_f11.png)|


### 5. EDGWO v.s. EDGWO_Kao
#### 停滯檢測與重置 ()：
* 演算法會監控最佳適應度，若在一定周期內內進步幅度小於設定的容忍值，則判定演算法陷入停滯。
* 觸發重置時，會將表現最差的 $15\%$ 個體，在當前最佳解附近以一定半徑內範圍重新生成，藉此跳脫局部最佳解，該半徑會隨時間而縮短。
```python
# 1. Stagnation Detection
tolerance = 1e-5
if (prev_f_alpha - f_alpha) < tolerance:
    counter += 1
else:
    counter = 0
    prev_f_alpha = f_alpha
    
if counter >= patient:
    worst_indices = np.argsort(curr_scores)[-replace_num:]
    radius = (UB - LB) * 0.2 * (1 - t / tmax)
    X[worst_indices] = X_alpha + np.random.uniform(-radius, radius, (replace_num, Dim))
    counter = 0
```

#### 多樣性動態參數：
* 棄用原版線性遞減的參數 $a$，改採非線性遞減策略：$a = 2 \times (1 - (t / t_{max})^2)$。
* 每次迭代計算群體多樣性比例 div_ratio。當處於探索前中期且群體多樣性大幅下降時，強制將收斂參數 $a$ 拉高，以恢復群體的探索能力。

```python
# 2. Diversity-Driven Parameter Adaptation
X_m = np.mean(X, axis=0)
curr_div = np.mean(np.linalg.norm(X - X_m, axis=1))

if t == 0:
    max_div = curr_div
    
div_ratio = curr_div / (max_div + 1e-10)
a = 2 * (1 - (t / tmax)**2)

if div_ratio < 0.1 and t < 0.7 * tmax:
    a = min(2.0, a + 0.5) 
```

## Conclusion
本專案重現了 EDGWO 的演算法機制，並且提出嘗試優化的 EDGWO_Kao 版本。藉由在標準 CEC2021 與 CEC2022 基準測試集上的驗證，EDGWO_Kao 在部分資料集能夠有超越 EDGWO 的表現，表示本專案所引入的「停滯偵測重置」與「多樣性驅動」設計能更有效地避免早熟收斂，並在全域探索與局部開發中取得更佳的平衡。

## Author
**Shao-Lun Kao**  
*B.S. in Computer Science and Engineering, National Sun Yat-sen University (NSYSU)*