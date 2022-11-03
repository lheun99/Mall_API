# Mall-API

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### API Documentation

[Mall API Documentation](https://documenter.getpostman.com/view/19591285/2s8YKFGiCy)

### SQL

#### 1. 총매출

```sql
select date_trunc('day', "Order".ordered_at) as "일자", sum("Order".quantity*"Product".price) as "총 매출"
from "Order"
inner join "Product"
ON "Order".product_id="Product".id
group by date_trunc('day', "Order".ordered_at)
order by date_trunc('day', "Order".ordered_at)
```

#### 2. 제품별 판매수량

```sql
select date_trunc('day', "Order".ordered_at) as "일자", "Product".product_name as "제품 이름" , sum("Order".quantity) as "판매 수량"
from "Order"
inner join "Product"
ON "Order".product_id="Product".id
group by "Product".id, date_trunc('day', "Order".ordered_at)
order by date_trunc('day', "Order".ordered_at)

```

#### 3. 제품별 매출

```sql
select date_trunc('day', "Order".ordered_at) as "일자", "Product".product_name as "제품 이름", sum("Order".quantity*"Product".price) as "매출"
from "Order"
inner join "Product"
ON "Order".product_id="Product".id
group by "Product".id, date_trunc('day', "Order".ordered_at)
order by date_trunc('day', "Order".ordered_at)
```
