# Delta

Прототип оффлайн-программы “Wollie” готовый для интеграции с моделью искуственного интеллекта.

![Mask group2](https://user-images.githubusercontent.com/45436388/170848698-94a45f76-ca23-4616-ad30-3873a786918e.png)

### Стек технологий: 
+ Frontend (PyQt5, Qt designer)
+ Backend (Python)

### Примеры работы
Выбор директории с набором фотографий

![1](https://user-images.githubusercontent.com/45436388/170848184-f53387c6-af6a-41ee-a053-ee26529379e8.jpg)
![2](https://user-images.githubusercontent.com/45436388/170848188-b4dd63ff-01fb-4615-b5b7-1fb73c0b8949.jpg)

Основной интерфейс программы

![3](https://user-images.githubusercontent.com/45436388/170848190-19b7d72c-1307-4d50-8ce2-d878598efdaf.jpg)
![4](https://user-images.githubusercontent.com/45436388/170848191-27c9610f-7ced-454e-89dd-43ce3e19c716.jpg)

Возможность просмотра метаданных фотографий, в частности GPS координат, времени и места съёмки

![5](https://user-images.githubusercontent.com/45436388/170848192-68c662b3-2086-482f-bb77-512fe1fc678b.jpg)

Отображение GPS координат для одной или всех фотографий на карте

![6](https://user-images.githubusercontent.com/45436388/170848194-2535dbee-cd13-4db1-8f5a-898b4ee65d1d.jpg)
![7](https://user-images.githubusercontent.com/45436388/170848197-d6d5a38c-51d5-4770-932f-3caf3d1d8bdf.jpg)

Расчет. Интерфейс для интеграции ИИ.

![8](https://user-images.githubusercontent.com/45436388/170848199-ecd74338-9fbb-4091-a9ac-8ebc5d8a471a.jpg)

Пример файла с данными и результатами. В формате: имя фото; дата; время; широта; долгота; количество

![9](https://user-images.githubusercontent.com/45436388/170848202-401f0021-eb2a-4539-9da1-64f15251f1fd.jpg)

Возможность создания excel файла на основе текстовго файла с результатами

![10](https://user-images.githubusercontent.com/45436388/170848208-c1635708-09a3-446c-a65b-d3d97d994913.jpg)
![11](https://user-images.githubusercontent.com/45436388/170848211-cbe9a521-a196-4a9c-8e60-0aa08df71c4c.jpg)



### Запуск в windows 10:
Зависимости:

-pip install pillow

-pip install exifread

-pip install pandas

-pip install PyQt5

-запустить gallery.pyw

-если запускать через cmd: python путь/gallery.pyw
При этом терминал запустить из папки с программой
