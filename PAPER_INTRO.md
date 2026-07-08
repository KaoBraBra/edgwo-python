# EDGWO algorithm overview

## Introduction
根據論文內容，EDGWO 與傳統 GWO 的主要差別在於，EDGWO 解決了傳統 GWO 容易陷入局部最佳解、過早收斂以及探索與開發能力不平衡的缺點。

### 引入社會階層與雙層搜尋策略
* **GWO**：狩獵機制較為單一，主要依賴 Alpha、Beta 和 Delta 狼的資訊來引導整個狼群進行包圍與攻擊 。
* **EDGWO**：結合灰狼社會階層，將狼群劃分為精英層與普通層。演算法為 Alpha、Beta 和 Delta 狼設計了 global exploration operators 與 local exploitation operators，強化了在全局解空間中的探索能力 。

### 動態適應的搜尋機制
* **GWO**：隨著參數線性遞減，灰狼個體在解空間中的移動傾向一致，容易在優化後期失去探索多樣性。
* **EDGWO**：根據動態搜尋參數 $\vec{A}$ 的變化，實時調整 Alpha、Beta 和 Delta 狼的搜尋行為 。這讓演算法在早期能廣泛且快速地覆蓋解空間，而在後期則能平滑過渡，專注於有潛力的區域進行深度開發，有效提升解的品質並避免陷入局部最佳解。

### Omega 狼的隨機機率搜尋機制
* **GWO**：Omega 狼只能被動跟隨 Alpha、Beta 和 Delta 狼的引導進行攻擊，這會削弱狼群整體的探索能力並增加陷入局部最佳解的風險。
* **EDGWO**：引入了隨機機率值 $p$，賦予 Omega 狼在局部開發與全局探索之間靈活隨機切換的能力。此機制增加了搜尋過程的隨機性、不可預測性與多樣性，有效避免了演算法過早收斂。

## Pseudo code
以下是 EDGWO 的 pseudo code
```text
Algorithm 1: Pseudo Code of EDGWO Algorithm

Input: 
  N: 狼群數量 (Population size)
  t_max: 最大迭代次數 (Maximum iterations)
  D: 搜尋空間維度 (Dimensional search space)
Output: 
  最佳解向量 (Alpha 狼的位置) X_alpha

1. 初始化相關參數與灰狼群體位置;
2. 計算群體中每個個體的適應度值 f(X_i)，並記錄排名前三的最佳位置 X_alpha, X_beta, 以及 X_delta;
3. while ( t < t_max ) do
4.     根據公式 (11) 計算目前灰狼群體的平均位置 X_m(t);
5.     for i = 1 to N do
6.         根據公式 (2) 和 (3) 計算控制參數 A_1, A_2, A_3 和 C_1, C_2, C_3 的值;
7.         產生一個區間在 [0,1] 之間的隨機數 p;
8.         
           // 決定 Alpha 狼的更新方式
9.         if (|A_1| < 1) then
10.            區域開發-I 階段：根據公式 (4) 更新 X_1 的位置;
11.        else
12.            全局探索-I 階段：根據公式 (8) 更新 X_1 的位置;
13.        end if

           // 決定 Beta 狼的更新方式
14.        if (|A_2| < 1) then
15.            區域開發-II 階段：根據公式 (5) 更新 X_2 的位置;
16.        else
17.            全局探索-II 階段：根據公式 (9) 更新 X_2 的位置;
18.        end if

           // 決定 Delta 狼的更新方式
19.        if (|A_3| < 1) then
20.            區域開發-III 階段：根據公式 (6) 更新 X_3 的位置;
21.        else
22.            全局探索-III 階段：根據公式 (10) 更新 X_3 的位置;
23.        end if

           // 決定 Omega 狼 (個體) 的最終更新方式
24.        if (p < 0.5) then
25.            區域開發-IV 階段：根據公式 (7) 更新個體位置 X_i(t+1);
26.        else
27.            全局探索-IV 階段：根據公式 (12) 更新個體位置 X_i(t+1);
28.        end if
29.    end for

30.    重新計算更新後群體的適應度值 f(X_i);
31.    更新目前為止最佳的三個位置 X_alpha, X_beta, 和 X_delta;
32.    t = t + 1;
33. end while
34. 輸出最佳解 X_alpha
```
---

## Explanation
### 1. 灰狼群體平均位置
在每次迭代中，演算法會先計算整個狼群的平均位置，這是為了在全局探索階段引導狼群 。

$$\vec{X_m}(t) = \frac{1}{N} \sum_{i=1}^{N} \vec{X_i}(t)$$

* **$\vec{X_m}(t)$**：在第 $t$ 次迭代時，灰狼群體的平均位置 。
* **$N$**：群體中灰狼的總數量 。
* **$\vec{X_i}(t)$**：第 $i$ 隻灰狼在第 $t$ 次迭代時的位置 。



---

### 2. 演算法控制參數
這是控制灰狼行為（靠近獵物或遠離獵物）的兩個關鍵參數向量 。

$$\vec{A} = 2 \cdot \vec{a} \cdot \vec{r_1} - \vec{a}$$

$$\vec{C} = 2 \cdot \vec{r_2}$$

* **$\vec{A}$**：決定搜尋方向與步長的隨機向量。當 $|\vec{A}| < 1$ 時進行區域開發，當 $|\vec{A}| > 1$ 時進行全局探索 。
* **$\vec{C}$**：表示灰狼接近獵物的難易程度，為最佳化過程增加隨機性 。
* **$\vec{a}$**：一個隨著迭代次數從 2 線性遞減到 0 的控制參數，公式為 $\vec{a} = 2 - t \times (\frac{2}{t_{max}})$ 。
* **$t$**：當前的迭代次數 。
* **$t_{max}$**：最大迭代次數 。
* **$\vec{r_1}, \vec{r_2}$**：介於 [0, 1] 之間的隨機向量 。

---

### 菁英狼的引導位置計算
#### 區域開發階段(Local Exploitation) :

當 $|\vec{A}|< 1$ 時，演算法進入區域開發階段，此時採用傳統 GWO 的機制，讓狼群向 Alpha、Beta 和 Delta 狼靠近。

$$\vec{X_1} = \vec{X_\alpha}(t) - \vec{A_1} \cdot \vec{D_\alpha}$$

$$\vec{X_2} = \vec{X_\beta}(t) - \vec{A_2} \cdot \vec{D_\beta}$$

$$\vec{X_3} = \vec{X_\delta}(t) - \vec{A_3} \cdot \vec{D_\delta}$$

* **$\vec{X}(t)$**：灰狼個體目前的位置 。
* **$\vec{X_\alpha}(t), \vec{X_\beta}(t), \vec{X_\delta}(t)$**：分別代表當前最優的三隻狼（Alpha, Beta, Delta）的位置 。
* **$\vec{A_1}, \vec{A_2}, \vec{A_3}$**：對應三隻菁英狼的 $\vec{A}$ 參數值 。
* **$\vec{D_\alpha}, \vec{D_\beta}, \vec{D_\delta}$**：個體灰狼與這三隻菁英狼之間的距離向量。例如 $\vec{D_\alpha} = |\vec{C_1} \cdot \vec{X_\alpha}(t) - \vec{X}(t)|$ 。

#### 全局探索階段(Global Exploration) :

這是 EDGWO 提出的核心改良機制，當 $|\vec{A}| > 1$ 時觸發，此時採用 EDGWO，讓狼群有機會探索四周。

$$\vec{X_1} = (\vec{X_\alpha}(t) - \vec{X_m}(t)) - \vec{r_3} \cdot (\vec{LB} + \vec{r_4} \cdot (\vec{UB} - \vec{LB}))$$

$$\vec{X_2} = (\vec{X_\beta}(t) - \vec{X_m}(t)) - \vec{r_3} \cdot (\vec{LB} + \vec{r_4} \cdot (\vec{UB} - \vec{LB}))$$

$$\vec{X_3} = (\vec{X_\delta}(t) - \vec{X_m}(t)) - \vec{r_3} \cdot (\vec{LB} + \vec{r_4} \cdot (\vec{UB} - \vec{LB}))$$

* **$\vec{X}(t)$**：灰狼個體目前的位置 。
* **$\vec{X_\alpha}(t), \vec{X_\beta}(t), \vec{X_\delta}(t)$**：分別代表當前最優的三隻狼（Alpha, Beta, Delta）的位置 。
* **$\vec{X_m}(t)$**：前面計算出的群體平均位置，用以擴大全局搜尋範圍 。
* **$\vec{r_3}, \vec{r_4}$**：介於 [0, 1] 之間的隨機向量，用來隨機縮放邊界，增加探索多樣性 。
* **$\vec{LB}, \vec{UB}$**：搜尋空間的下界 (Lower Bound) 與上界 (Upper Bound) 。

---

### Omega 狼的最終位置更新
#### 區域開發階段(Local Exploitation) :

當 $p < 0.5$ 時，演算法進入區域開發階段，此時採用傳統 GWO 的機制，讓狼群向 Alpha、Beta 和 Delta 狼靠近。

$$\vec{X_i}(t+1) = \frac{\vec{X_1} + \vec{X_2} + \vec{X_3}}{3}$$

* **$\vec{X}(t)$**：灰狼個體目前的位置 。

#### 全局探索階段(Global Exploration) :

這是 EDGWO 提出的核心改良機制，當 $p > 0.5$ 時觸發，此時採用 EDGWO，讓狼群有機會探索四周。

$$\vec{X_i}(t+1) = \vec{X_\alpha}(t) + |\vec{X_\alpha}(t) - \vec{X_i}(t)| \cdot e^l \cdot \cos(2\pi \cdot \vec{l})$$

* **$\vec{X}(t)$**：灰狼個體目前的位置 。
* **$\vec{X_\alpha}(t), \vec{X_\beta}(t), \vec{X_\delta}(t)$**：分別代表當前最優的三隻狼（Alpha, Beta, Delta）的位置 。
* **$e^l \cdot \cos(2\pi \cdot \vec{l})$**：螺旋形狀的更新運算子，引導 Omega 狼以螺旋方式朝 Alpha 狼的方向移動，確保探索方向的多樣性 。
* **$\vec{l}$**：控制螺旋形狀的隨機參數，計算方式為 $\vec{l} = -1 + 2 \cdot \vec{r_5}$，其中 $\vec{r_5}$ 為 [0, 1] 之間的隨機向量 。

---