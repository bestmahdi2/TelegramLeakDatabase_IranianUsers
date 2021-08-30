# :computer: Telegram Leak Database Of Iranian Users | دیتابیس یوزرهای تلگرام - سامانه شکار
**This repository does not promote or encourage Any illegal activities; all contents provided by these databases are meant for informing, examining, analyzing, and educational purposes only.**

Because of the massive size of files and GitHub's rules, there are only tests files in the "Test" folder, and for downloading the complete database, you should go to this Telegram channel ([Downloads](#floppy_disk-Download)).

<div dir="rtl">

---
**مسئولیت استفاده از این دیتابیس بر عهده ی خود شخص است. این اطلاعات فقط برای آنالیز ، طبقه بندی و اطلاع میباشد.**

**به دلیل حجم بالای فایل ها و قوانین گیتهاب ، فقط پوشه ی تست قرار داده شده که میتوانید برای تست از آن استفاده کنید. برای دانلود کامل دیتابیس به این کانال تلگرام مراجعه کنید. ([دانلود](#floppy_disk-دانلود))**
</div>

## :mag_right: Menu | فهرست

* English | انگلیسی
  * [Python Files](#snake-Python-Files)
  * [Test Directory Files & Folders](#hash-Test-Directory-Files-and-Folders)
  * [Access Data](#key-Access-Data)
  * [Useful SQLite commands](#white_check_mark-Useful-SQLite-commands)
  * [Protect Yourself](#shield-How-to-protect-yourself)
  * [Notes](#warning-Notes)
  * [Downloads](#floppy_disk-Download)
 

* Persian | فارسی
  * [فایل های پایتون](#snake-فایل-های-پایتون)
  * [فایل ها و پوشه های داخل پوشه ی تست](#hash-فایل-ها-و-پوشه-های-داخل-پوشه-ی-تست)
  * [دسترسی به اطلاعات](#key-دسترسی-به-اطلاعات)
  * [دستور های کاربردی اسکوئلایت](#white_check_mark-دستور-های-کاربردی-اسکوئلایت)
  * [چطور از خود محافظت کنید](#shield-چطور-از-خود-محافظت-کنید)
  * [نکات](#warning-نکات)
  * [دانلود](#floppy_disk-دانلود)

# :arrow_right: English | انگلیسی

## :snake: Python Files
#### Creat_New_Database.py:
This file is for creating a new empty SQLite database (.db). You can also change its name or its location.

#### Leaked_2_DB_&_TXT.py:
This file is for reading, converting, exporting, and descending the data from initial databases (.txt files).

**Note:** If you don't have the initial database, this file is not helpful to you.
Put txt files in the "database" folder where this file is, and run. It will create a light version of txt files and also create an SQLite database from them. You can also change its name or its location.

---

## :hash: Test Directory Files and Folders
**Note:** This directory is only for tests. You can download the complete files from [Downloads](#floppy_disk-Download).

#### LightTXT: 
It contains light version files of all initial databases in txt.

#### LightDB.db:
It contains all 41 million entries were in initial txt files. About 5 million of them are duplicated data deleted in "LightDB_no_dup.db" and "LightCSV_no_dup.csv".

#### LightDB_no_dup.db:
It contains 35,319,059 entries of users. It has about 42,000 duplicated "id"s with different "username"s, or users deleted them on other dates.

#### LightCSV_no_dup.csv:
It contains 35,319,059 entries of users. It has about 42,000 duplicated "id"s with different "username"s, or users deleted them on other dates.

---

## :key: Access Data
#### Use TXT:
To read this file, you can use "EmEditor". Try not to use basic text editors like "Notepad".

#### Use CSV:
To read this file, you can use "Microsoft Excel" or "EmEditor".

#### Use SQLite (.db):
You can use database management software such as "Navicat".

---

## :white_check_mark: Useful SQLite commands
**Note:** To execute these commands in python,

    import sqlite3
    Connection = sqlite3.connect("name.db")
    Connection.execute("sqlite command ...")
    Connection.commit()

### Create a table:
    CREATE TABLE IF NOT EXISTS People (UID integer PRIMARY KEY, id integer NOT NULL, phone integer NOT NULL, username text)")

### Find Duplicated Rows:
    SELECT id, COUNT(*) counter FROM People GROUP BY id HAVING counter > 1;

### Remove Duplicated Rows:
    DELETE FROM People WHERE rowid NOT IN (SELECT MIN(rowid) FROM People GROUP BY id, phone, username)

### Find a row by id:
    SELECT UID,id,phone,username FROM People WHERE id = 123456789

### Find a row by phone:
    SELECT UID,id,phone,username FROM People WHERE phone = 989123456789

### Find a row by username:
    SELECT UID,id,phone,username FROM People WHERE username = @abcdefgij

---

## :shield: How to protect yourself 
### if your id, phone number, or username were in the database:
This database won't harm anyone, and people can only find your phone number or username by id. There are some steps for those who don't want their information to be in this database anymore. 
1. By deleting your Telegram account and rejoining, Telegram will give you a new id, so people can't find you by id anymore.
2. If you can't delete your account, you can change your username and phone number to prevent people from reaching your information.

---

## :warning: Notes
In the initial database, there is other information, like the first name, last name, profile photo location, your last seen status, and some more. But this information isn't valuable or even valid. All names are fake, and others are old, so there is nothing to worry about.
For more information, you can visit this [Persian site](https://memoryleaks.ir/analysis-of-42m-leaked-telegram-data/). (Use Google translate for this page)

---

## :floppy_disk: Download
You can download complete databases in this [Telegram channel](https://t.me/DbTelLeakIranHaunting).


---

<div dir="rtl">

# :arrow_right: Persian | فارسی

## :snake: فایل های پایتون
#### Creat_New_Database.py:
این فایل برای ایجاد یک دیتابیس SQLite خالی با پسوند db است. میتوانید اسم یا محل آن را در فایل تغییر دهید.

#### Leaked_2_DB_&_TXT.py:
این فایل برای خواندن ، تبدیل ، خارج سازی اطلاعات و کم حجم کردن دیتابیس اصلی (فایل با پسوند txt) است.

**نکته:** اگر دیتابیس اصلی را ندارید ، این فایل کمکی به شما نمیکند. فایل های txt را در پوشه ی database در محلی که این فایل هست قرار داده و آن را اجرا کنید. این فایل فایل های متنی با حجم کمتر و همچنین یک دیتابیس سبک شده با SQLite از آن ها میسازد. همچنین میتوانید اسم و مسیر آن تغییر دهید.

---

## :hash: فایل ها و پوشه های داخل پوشه ی تست
**نکته:** این پوشه فقط برای تست بوده و برای دانلود کامل فایل ها به قسمت [دانلود](#floppy_disk-دانلود) مراجعه کنید.

#### LightTXT:
این پوشه نسخه ی سبک دیتابیس اصلی را در قالب txt را دارد.

#### LightDB.db:
این فایل همه ی 41 میلیون مدخلی که در فایل های txt اصلی موجود بود را دارد. نزدیک 5 میلیون از آن ها تکراری بوده که در دو فایل "LightDB_no_dup.db" و "LightCSV_no_dup.csv" حذف شده اند.

#### LightDB_no_dup.db:
این فایل 35,319,059 مدخل از کابران دارد. حدود 42 هزار id با username های متفاوت وجود دارد که ممکن است توسط خود کاربر پاک شده یا عوض شده باشند.

#### LightCSV_no_dup.csv:
این فایل 35,319,059 مدخل از کابران دارد. حدود 42 هزار id با username های متفاوت وجود دارد که ممکن است توسط خود کاربر پاک شده یا عوض شده باشند.

---

## :key: دسترسی به اطلاعات
#### TXT:
برای خواندن این فایل بهتر است از "EmEditor" استفاده کنید. از برنامه های ویرایشگر متن ساده مثل "Notepad" استفاده نکنید.

#### CSV:
برای خواندن این فایل بهتر است از "Microsoft Excel" یا "EmEditor" استفاده کنید.

#### SQLite (.db):
برای خواندن این فایل میتوانید از برنامه های مدیریت دیتابیس مثل "Navicat" استفاده کنید.

---

## :white_check_mark: دستور های کاربردی اسکوئلایت
**نکته:** برای استفاده از این دستور ها در زبان پایتون،
<div dir="ltr">

    import sqlite3
    Connection = sqlite3.connect("name.db")
    Connection.execute("sqlite command ...")
    Connection.commit()
</div>

### ساخت یک جدول: 
<div dir="ltr">

    CREATE TABLE IF NOT EXISTS People (UID integer PRIMARY KEY, id integer NOT NULL, phone integer NOT NULL, username text)")
</div>

### پیدا کردن ردیف های تکراری: 
<div dir="ltr">

    SELECT id, COUNT(*) counter FROM People GROUP BY id HAVING counter > 1;
</div>

### پاک کردن ردیف های تکراری: 
<div dir="ltr">

    DELETE FROM People WHERE rowid NOT IN (SELECT MIN(rowid) FROM People GROUP BY id, phone, username)
</div>

### پیدا کردن یک ردیف با آیدی: 
<div dir="ltr">

    SELECT UID,id,phone,username FROM People WHERE id = 123456789
</div>

### پیدا کردن یک ردیف با شماره تلفن: 
<div dir="ltr">

    SELECT UID,id,phone,username FROM People WHERE phone = 989123456789

</div>

### پیدا کردن یک ردیف با نام کاربری: 
<div dir="ltr">

    SELECT UID,id,phone,username FROM People WHERE username = @abcdefgij
</div>

---

## :shield: چطور از خود محافظت کنید
### اگر آیدی ، شماره تلفن یا نام کاربری شما در این دیتابیس موجود است: 
این دیتابیس آسیب رسان نیست و فقط میتوان از آن برای پیدا کردن نام کاربری یا شماره تلفن شما از آیدی عددی استفاده کرد. چند راه برای کسانی وجود دارد که نمیخواهند اطلاعات آن ها در این دیتابیس باشد:
1. با پاک کردن اکانت تلگرام خود و ورود دوباره، تلگرام به شما یک آیدی عددی جدید میدهد، پس دیگران نمیتوانند شما را بر اساس آیدی عددی پیدا کنند.
2. اگر نمیتوانید اکانت خود را حذف کنید، میتوانید با تغییر شماره تلفن و نام کاربری خود، از دسترسی افراد به اطلاعات شما جلوگیری کنید.

---

## :warning: نکات
در دیتابیس اصلی و خام، اطلاعات بیشتری نیز وجود دارد از جمله: نام و نام خانوادگی ، مکان عکس پروفایل ، وضعیت آخرین بازدید شما و غیره. اما این اطلاعات باارزش و معتبر نیستند. تمامی نام ها تقلبی بوده و بقیه ی اطلاعات نیز قدیمی هستند ، پس جای نگرانی ای نیست. برای اطلاعات بیشتر ، میتوانید این [سایت](https://memoryleaks.ir/analysis-of-42m-leaked-telegram-data/)
 را مشاهده کنید.

---

## :floppy_disk: دانلود
برای دانلود دیتابیس کامل به این [کانال تلگرام](https://t.me/DbTelLeakIranHaunting) مراجعه کنید.

</div>
