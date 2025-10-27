1. Install Dependencies

Run the below command in your terminal:

pip install pandas matplotlib scikit-learn

2. In your project folder, run:

python customer_segmentation.py

OUTPUT:
Loaded 20 rows
   CustomerID  Age  Income  SpendingScore
0           1   19   15000             39
1           2   35   35000             81
2           3   26   40000              6
3           4   27   45000             77
4           5   19   20000             40

Cluster counts:
0    6
1    5
2    4
3    5
Name: Cluster, dtype: int64

Cluster means:
         Age   Income  SpendingScore
Cluster
0       27.5  20000.0          58.4
1       38.8  75000.0          20.0
2       23.0  32000.0          65.0
3       43.0  95000.0          10.0
