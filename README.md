[ссылка на схему бд](https://dbdiagram.io/d/6481eb55722eb77494a30331)

Сайт представляет из себя магазин продажи кукол. Состоит из пяти страниц: "Главная" (Home) с товарами; "О нас" (About Us) с описанием магазина, "Контакты" (Contact) с телефоном, почтой и формой фидбека (почта+текст) для обратной связи, "Отзывы" (Feedback), "Корзина" (Basket) для красоты.
К "Главной странице" (Home) на отображение подключена таблица из БД с товарами (items), редактируемая через Django Administration. Таблица (items) состоит из атрибутов id, image, name, price.
К странице "Контакты" (Contact) на сбор данных подключена таблица из БД с фидбеками (feedback), редактируемая через Django Administration. Таблица (feedback) состоит из атрибутов id, email, text. 
К странице "Отзывы" (Feedback) на отображение подключена таблица из БД с фидбеками (feedback), редактируемая через Django Administration. Таблица (feedback) состоит из атрибутов id, email, text. 
К сайту так же подключены таблицы заказов (orders) и клиентов (clients), но на сайте они нигде не отображаются, поскольку их потенциал не раскрыт за ненадобностью.
