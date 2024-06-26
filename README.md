## **Problem: 拼圖大師**

#### **問題描述**

​	**學期末快到了，作為學生的你被要求要設計一款小遊戲，你決定開發一款名為「拼圖大師」的遊戲，通過拼圖檔案的讀取，玩家可以在一個 8x8 的盤面上放置各種形狀的拼圖，最後輸出拼圖結果，已知拼圖規則如下：**

1. **拼圖的種類**

   **每個拼圖會以一個txt檔案存在一個資料夾中(資料夾名稱取決於程式碼第一行的輸入)，而txt檔案中存放的資料代表一個拼圖的長相如下圖一 (a) 所示：**

   **<img src=".\images\img1.png" align="left" />**

   **上圖為一個名為H7的拼圖(H7表示顏色代碼)，在文件內容中，0代表拼圖空心處而H7代表拼圖實心處，如上圖一(b)所示，這個拼圖H7為一個”H”型拼圖。**

   

2. **拼拼圖規則**

   **所有拼圖將以「拼圖代號(檔名)」的ASCII順序由小到大取出並拼湊到8x8 的盤面上，且拼法將依循「由左到右，由上到下」的方式進行拼湊，如下圖二所示。**

   **<img src=".\images\img2.png" align="left" />**

   **如上圖二所示，左邊拼圖代號為F5，右邊為H7，依照ASCII順序由小到大應先取出F5拼湊至8x8的盤面中；接下來，拼圖H7將依循「由左到右，由上到下」的方式再次拼湊至盤面中，如下圖三所示。**
   
   **<img src=".\images\img3.png" style="zoom:50%;" align="left"/>**



**根據以上規則，請實作一個程式碼，讀取資料夾中的所有拼圖檔案，將這些拼圖依序拼到一個8x8的盤面中，拼圖過程中不可出現拼圖與拼圖之間兩兩覆蓋的情況，拼圖本身也不可超出盤面。請計算可以使用的最大拼圖數，並將拼圖結果一起寫入一個txt檔中。**

**其中，**

- **拼圖不會旋轉，但有可能超出盤面大小**
- **一個拼圖只會有一個顏色**
- **拼圖檔名必等同顏色代碼(顏色代碼為H7的拼圖檔名必為H7.txt)**



#### **實作限制**

- **使用java.io套件中的package讀取資料夾中拼圖檔案的資訊**
- **實作以下兩個function去進行讀檔與寫檔的動作，而對於每一個讀寫檔動作，均需實作try-catch機制去處理讀寫檔失敗時的情況**

**以上函示中的傳入參數請勿修改或刪除，但可新增，函數回傳型別也可自行更改。未按規定方式實作將予以扣分。**

**<img src=".\images\img4.png"/>**  





#### **輸入說明**

- **第一行請輸入一個字串，代表存放拼圖檔案的資料夾名稱**

- **在輸入的資料夾底下，存放一連串的txt檔案，代表每個拼圖長相，其中資料夾結構如下所示(假設資料夾名稱為puzzles)**

  **<img src=".\images\img5.png"/>**



#### **輸出說明**

**將以下資訊寫入一個txt檔案中：**

- **第一行請寫入We use 使用拼圖數量 pieces of puzzles.**
- **接下來寫入拼圖結束後的8x8盤面長相**

**其中，輸出檔檔名請命名為 {存放拼圖資料夾名稱}_{你的學號}.txt。(假設資料夾名稱為puzzles，則輸出檔名稱請命名為puzzles_112XXXXXX.txt)**



#### **範例**

**<img src=".\images\img6.png"/>**

**<img src=".\images\img7.png"/>**



#### **範例說明**
| **Sample Content in Output 1** | <img src=".\images\img8.png"/> |
| ------------------------------ | ---------------------- |
| **Sample Content in Output 2** | <img src=".\images\img9.png"/> |



#### **附件檔說明**

本次作業將額外提供一個ShowResult.java檔案，用以列印出拼圖長相以供參考，使用方式如下：

```java
new ShowResult(board);
```

其中`board`必須是`ArrayList<String[]>`型別，代表整個盤面/拼圖的長相，`String[]`陣列中存放的值為`”0”`或是顏色代碼(ex. `”H7”`)。將`ShowResult.java`與`A07_112XXXXXX.java`放在同一個資料夾底下執行即可印出`board`的圖像。(使用前請先確保`package`是否正確，Eclipse使用方式請參照附件mp4檔)

**請注意，`ShowResult.java`僅作為工具使用，繳交作業前請將`new ShowResult(board);`的程式碼刪除，否則批改作業時檔案將無法執行。**



## **系統介紹**

#### **I. 解壓縮**

```cmd
python a07_unzip.py
```

**以下資料放一起**

* **學生作業 zip 檔**
* **`a07_unzip.py`**



#### **II. 註解掉 package assignment**

```cmd
python comment.py
```

**以下資料放一起**

* **files 資料夾(裡面存放學生作業 java 檔)**
* **`comment.py`**



#### **III. 編譯並執行**

```cmd
python compile_run.py
```

**以下資料放在一起**

* **`puzzles1` ~ `puzzles10` 的資料夾**
* **`1.in` ~ `10.in` 檔案**
* **`compile_run.py`**
* **學生的 `.java` 檔**



#### **IV. 一鍵執行**

**將所有檔案放置於相同資料夾下，直接執行 `main.py` 即可，`move.py` 用於移動相關檔案。**



## **測資檔案連結**

**https://drive.google.com/file/d/1sJFjqKuxX6WXTbsiwfBydfY3OrS7v_o8/view?usp=drive_link**
