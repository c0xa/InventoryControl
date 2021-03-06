PGDMP                         x            postgres    13.1    13.1 K    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    13442    postgres    DATABASE     e   CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Russian_Russia.1251';
    DROP DATABASE postgres;
                postgres    false            �           0    0    DATABASE postgres    COMMENT     N   COMMENT ON DATABASE postgres IS 'default administrative connection database';
                   postgres    false    3057            �           0    0    DATABASE postgres    ACL     �   GRANT ALL ON DATABASE postgres TO usertwo;
GRANT CONNECT ON DATABASE postgres TO main_user;
GRANT CONNECT ON DATABASE postgres TO secondary_user;
GRANT CONNECT ON DATABASE postgres TO user_two;
                   postgres    false    3057            �           0    0    SCHEMA public    ACL     �   GRANT USAGE ON SCHEMA public TO main_user;
GRANT USAGE ON SCHEMA public TO secondary_user;
GRANT USAGE ON SCHEMA public TO user_two;
                   postgres    false    4                        3079    16384 	   adminpack 	   EXTENSION     A   CREATE EXTENSION IF NOT EXISTS adminpack WITH SCHEMA pg_catalog;
    DROP EXTENSION adminpack;
                   false            �           0    0    EXTENSION adminpack    COMMENT     M   COMMENT ON EXTENSION adminpack IS 'administrative functions for PostgreSQL';
                        false    2            �            1255    16496    add_to_log()    FUNCTION     C  CREATE FUNCTION public.add_to_log() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
DECLARE
    mstr varchar(30);
    astr varchar(100);
BEGIN
    IF    TG_OP = 'INSERT' THEN
		UPDATE product SET count = count - NEW.countei  WHERE idproduct = NEW.codeproductei;
        RETURN NEW;
    ELSIF TG_OP = 'UPDATE' THEN
		if OLD.codeproductei = NEW.codeproductei THEN
			UPDATE product SET count = count - NEW.countei + OLD.countei  WHERE idproduct = NEW.codeproductei;
		ELSE
			UPDATE product SET count = count - NEW.countei WHERE idproduct = NEW.codeproductei;
			UPDATE product SET count = count + OLD.countei WHERE idproduct = OLD.codeproductei;
		 END IF;
        RETURN NEW;
    ELSIF TG_OP = 'DELETE' THEN
		UPDATE product SET count = count + OLD.countei  WHERE idproduct = OLD.codeproductei;
        RETURN OLD;
    END IF;
END;
$$;
 #   DROP FUNCTION public.add_to_log();
       public          postgres    false            �           0    0    FUNCTION add_to_log()    ACL     u   GRANT ALL ON FUNCTION public.add_to_log() TO main_user;
GRANT ALL ON FUNCTION public.add_to_log() TO secondary_user;
          public          postgres    false    234            �            1255    16498    add_to_log2()    FUNCTION     >  CREATE FUNCTION public.add_to_log2() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
DECLARE
    mstr varchar(30);
    astr varchar(100);
BEGIN
    IF    TG_OP = 'INSERT' THEN
		UPDATE product SET count = count + NEW.countRI WHERE idproduct = NEW.codeproductRI;
        RETURN NEW;
    ELSIF TG_OP = 'UPDATE' THEN
		if OLD.codeproductri = NEW.codeproductri THEN
			UPDATE product SET count = count + (NEW.countri - OLD.countri)  WHERE idproduct = NEW.codeproductri;
		ELSE
			UPDATE product SET count = count + NEW.countri WHERE idproduct = NEW.codeproductri;
			UPDATE product SET count = count - OLD.countri WHERE idproduct = OLD.codeproductri;
		END IF;
		RETURN NEW;
    ELSIF TG_OP = 'DELETE' THEN
		UPDATE product SET count = count - OLD.countri  WHERE idproduct = OLD.codeproductri;
        RETURN OLD;
    END IF;
END;
$$;
 $   DROP FUNCTION public.add_to_log2();
       public          postgres    false            �           0    0    FUNCTION add_to_log2()    ACL     w   GRANT ALL ON FUNCTION public.add_to_log2() TO main_user;
GRANT ALL ON FUNCTION public.add_to_log2() TO secondary_user;
          public          postgres    false    235            �            1255    16473    countproduct()    FUNCTION     �   CREATE FUNCTION public.countproduct() RETURNS integer
    LANGUAGE plpgsql
    AS $$
declare
	total integer;
BEGIN
   SELECT count(*) into total  FROM product;
   RETURN total;
END;
$$;
 %   DROP FUNCTION public.countproduct();
       public          postgres    false            �            1255    16450    delete_data(integer) 	   PROCEDURE     �   CREATE PROCEDURE public.delete_data(id_person integer)
    LANGUAGE sql
    AS $$
DELETE FROM person WHERE idperson = id_person
$$;
 6   DROP PROCEDURE public.delete_data(id_person integer);
       public          postgres    false            �            1255    16452 "   delete_expenditureinvoice(integer) 	   PROCEDURE     �   CREATE PROCEDURE public.delete_expenditureinvoice(id_expenditureinvoice integer)
    LANGUAGE sql
    AS $$
DELETE FROM expenditureinvoice WHERE idexpenditure = id_expenditureinvoice
$$;
 P   DROP PROCEDURE public.delete_expenditureinvoice(id_expenditureinvoice integer);
       public          postgres    false            �            1255    16515    delete_perfomance(integer) 	   PROCEDURE     �   CREATE PROCEDURE public.delete_perfomance(id_perfomance integer)
    LANGUAGE sql
    AS $$
DELETE FROM perfomance WHERE perfomance_id  = id_perfomance
$$;
 @   DROP PROCEDURE public.delete_perfomance(id_perfomance integer);
       public          postgres    false            �           0    0 2   PROCEDURE delete_perfomance(id_perfomance integer)    ACL     �   GRANT ALL ON PROCEDURE public.delete_perfomance(id_perfomance integer) TO main_user;
GRANT ALL ON PROCEDURE public.delete_perfomance(id_perfomance integer) TO secondary_user;
          public          postgres    false    237            �            1255    16451    delete_product(integer) 	   PROCEDURE     �   CREATE PROCEDURE public.delete_product(id_product integer)
    LANGUAGE sql
    AS $$
DELETE FROM product WHERE IdProduct = id_product
$$;
 :   DROP PROCEDURE public.delete_product(id_product integer);
       public          postgres    false            �            1255    16453    delete_receiptinvoice(integer) 	   PROCEDURE     �   CREATE PROCEDURE public.delete_receiptinvoice(id_receiptinvoice integer)
    LANGUAGE sql
    AS $$
DELETE FROM ReceiptInvoice WHERE idreceipt = id_ReceiptInvoice
$$;
 H   DROP PROCEDURE public.delete_receiptinvoice(id_receiptinvoice integer);
       public          postgres    false            �            1255    16456 A   edit_expenditureinvoice(date, integer, integer, integer, integer) 	   PROCEDURE     �  CREATE PROCEDURE public.edit_expenditureinvoice(dateei_new date, number_of_goodsei_new integer, persontab2 integer, producttab2 integer, expenditureinvoicetab2 integer)
    LANGUAGE sql
    AS $$
UPDATE expenditureinvoice SET dateei = dateei_new, CountEI  = Number_of_goodsEI_new,
     CodePersonEI = persontab2, CodeProductEI = producttab2
	 WHERE idexpenditure = expenditureinvoicetab2

$$;
 �   DROP PROCEDURE public.edit_expenditureinvoice(dateei_new date, number_of_goodsei_new integer, persontab2 integer, producttab2 integer, expenditureinvoicetab2 integer);
       public          postgres    false            �            1255    16519 I   edit_perfomance(character varying, date, date, double precision, integer) 	   PROCEDURE     r  CREATE PROCEDURE public.edit_perfomance(name_perfomance character varying, data_begin date, data_end date, price_new double precision, id_perfomance integer)
    LANGUAGE sql
    AS $$
UPDATE perfomance SET name_perfomance = name_perfomance, data_begin = data_begin, data_end = data_end, price = price_new::float8::numeric::money WHERE perfomance_id = id_perfomance
$$;
 �   DROP PROCEDURE public.edit_perfomance(name_perfomance character varying, data_begin date, data_end date, price_new double precision, id_perfomance integer);
       public          postgres    false            �           0    0 �   PROCEDURE edit_perfomance(name_perfomance character varying, data_begin date, data_end date, price_new double precision, id_perfomance integer)    ACL     i  GRANT ALL ON PROCEDURE public.edit_perfomance(name_perfomance character varying, data_begin date, data_end date, price_new double precision, id_perfomance integer) TO main_user;
GRANT ALL ON PROCEDURE public.edit_perfomance(name_perfomance character varying, data_begin date, data_end date, price_new double precision, id_perfomance integer) TO secondary_user;
          public          postgres    false    238            �            1255    16454 M   edit_person(character varying, character varying, character varying, integer) 	   PROCEDURE     <  CREATE PROCEDURE public.edit_person(firstname_new character varying, secondname_new character varying, patronymic_new character varying, id_person integer)
    LANGUAGE sql
    AS $$
UPDATE person SET firstname = firstname_new, secondname = secondname_new, patronymic = patronymic_new WHERE idperson = id_person
$$;
 �   DROP PROCEDURE public.edit_person(firstname_new character varying, secondname_new character varying, patronymic_new character varying, id_person integer);
       public          postgres    false            �            1255    16455 C   edit_product(integer, character varying, double precision, integer) 	   PROCEDURE     \  CREATE PROCEDURE public.edit_product(codeproduct_new integer, name_product_new character varying, price_new double precision, producttab integer)
    LANGUAGE sql
    AS $$
UPDATE product SET codeproduct = Codeproduct_new, nameproduct = Name_product_new
       ,price = Price_new::float8::numeric::money, count = 0 WHERE idproduct = producttab
$$;
 �   DROP PROCEDURE public.edit_product(codeproduct_new integer, name_product_new character varying, price_new double precision, producttab integer);
       public          postgres    false            �            1255    16457 =   edit_receiptinvoice(date, integer, integer, integer, integer) 	   PROCEDURE     q  CREATE PROCEDURE public.edit_receiptinvoice(dateri_new date, number_of_goodsri_new integer, persontab integer, producttab integer, receiptinvoicetab2 integer)
    LANGUAGE sql
    AS $$
UPDATE receiptinvoice SET DateRI = dateri_new, CountRI  = Number_of_goodsRI_new,
     CodePersonRI = persontab, CodeProductRI = producttab
	 WHERE idreceipt = receiptinvoicetab2

$$;
 �   DROP PROCEDURE public.edit_receiptinvoice(dateri_new date, number_of_goodsri_new integer, persontab integer, producttab integer, receiptinvoicetab2 integer);
       public          postgres    false            �            1255    16446 D   insert_data(character varying, character varying, character varying) 	   PROCEDURE        CREATE PROCEDURE public.insert_data(firstname character varying, secondname character varying, patronymic character varying)
    LANGUAGE sql
    AS $$
INSERT INTO person (firstname, secondname, patronymic) VALUES (firstname, secondname, patronymic);

$$;
 |   DROP PROCEDURE public.insert_data(firstname character varying, secondname character varying, patronymic character varying);
       public          postgres    false            �            1255    16514 <   insert_data(character varying, date, date, double precision) 	   PROCEDURE     4  CREATE PROCEDURE public.insert_data(name_perfomance character varying, data_begin date, data_end date, price double precision)
    LANGUAGE sql
    AS $$
INSERT INTO perfomance (name_perfomance, data_begin, data_end, price) VALUES (name_perfomance, data_begin, data_end, price::float8::numeric::money);

$$;
 ~   DROP PROCEDURE public.insert_data(name_perfomance character varying, data_begin date, data_end date, price double precision);
       public          postgres    false            �           0    0 p   PROCEDURE insert_data(name_perfomance character varying, data_begin date, data_end date, price double precision)    ACL     +  GRANT ALL ON PROCEDURE public.insert_data(name_perfomance character varying, data_begin date, data_end date, price double precision) TO main_user;
GRANT ALL ON PROCEDURE public.insert_data(name_perfomance character varying, data_begin date, data_end date, price double precision) TO secondary_user;
          public          postgres    false    236            �            1255    16448 :   insert_expenditureinvoice(date, integer, integer, integer) 	   PROCEDURE     #  CREATE PROCEDURE public.insert_expenditureinvoice(dateei date, countei integer, codepersonei integer, codeproductei integer)
    LANGUAGE sql
    AS $$
INSERT INTO expenditureinvoice (dateei, CountEI , CodePersonEI, codeproductEI) VALUES (dateei, CountEI , CodePersonEI, codeproductEI);
$$;
 |   DROP PROCEDURE public.insert_expenditureinvoice(dateei date, countei integer, codepersonei integer, codeproductei integer);
       public          postgres    false            �            1255    16447 <   insert_product(integer, character varying, double precision) 	   PROCEDURE     &  CREATE PROCEDURE public.insert_product(idproduct integer, nameproduct character varying, price double precision)
    LANGUAGE sql
    AS $$
INSERT INTO product (IdProduct, codeproduct, nameproduct, price, count) VALUES (IdProduct, IdProduct, nameproduct, price::float8::numeric::money, 0);
$$;
 p   DROP PROCEDURE public.insert_product(idproduct integer, nameproduct character varying, price double precision);
       public          postgres    false            �            1255    16449 6   insert_receiptinvoice(date, integer, integer, integer) 	   PROCEDURE       CREATE PROCEDURE public.insert_receiptinvoice(dateri date, countri integer, codepersonri integer, codeproductri integer)
    LANGUAGE sql
    AS $$
INSERT INTO ReceiptInvoice (dateri, CountRI , CodePersonRI, codeproductRI) VALUES (dateri, CountRI , CodePersonRI, codeproductRI);
$$;
 x   DROP PROCEDURE public.insert_receiptinvoice(dateri date, countri integer, codepersonri integer, codeproductri integer);
       public          postgres    false            �            1259    16405    product    TABLE     �   CREATE TABLE public.product (
    idproduct integer NOT NULL,
    codeproduct integer,
    nameproduct character varying(255) NOT NULL,
    price money,
    count integer
);
    DROP TABLE public.product;
       public         heap    postgres    false            �           0    0    TABLE product    ACL     �   GRANT UPDATE ON TABLE public.product TO usertwo;
GRANT ALL ON TABLE public.product TO main_user;
GRANT ALL ON TABLE public.product TO secondary_user;
GRANT ALL ON TABLE public.product TO user_two;
          public          postgres    false    203            �            1255    16481    productwatch(integer)    FUNCTION     �   CREATE FUNCTION public.productwatch(integer) RETURNS SETOF public.product
    LANGUAGE plpgsql
    AS $$
BEGIN
    RETURN QUERY SELECT * FROM public.product;
END;
$$;
 ,   DROP FUNCTION public.productwatch(integer);
       public          postgres    false    203            �            1259    16430    expenditureinvoice    TABLE     �   CREATE TABLE public.expenditureinvoice (
    idexpenditure integer NOT NULL,
    dateei date,
    countei integer,
    codepersonei integer,
    codeproductei integer
);
 &   DROP TABLE public.expenditureinvoice;
       public         heap    postgres    false            �           0    0    TABLE expenditureinvoice    ACL     �   GRANT UPDATE ON TABLE public.expenditureinvoice TO usertwo;
GRANT ALL ON TABLE public.expenditureinvoice TO main_user;
GRANT ALL ON TABLE public.expenditureinvoice TO secondary_user;
GRANT ALL ON TABLE public.expenditureinvoice TO user_two;
          public          postgres    false    207            �            1259    16412    receiptinvoice    TABLE     �   CREATE TABLE public.receiptinvoice (
    idreceipt integer NOT NULL,
    dateri date,
    countri integer,
    codepersonri integer,
    codeproductri integer
);
 "   DROP TABLE public.receiptinvoice;
       public         heap    postgres    false            �           0    0    TABLE receiptinvoice    ACL     �   GRANT UPDATE ON TABLE public.receiptinvoice TO usertwo;
GRANT ALL ON TABLE public.receiptinvoice TO main_user;
GRANT ALL ON TABLE public.receiptinvoice TO secondary_user;
GRANT ALL ON TABLE public.receiptinvoice TO user_two;
          public          postgres    false    205            �            1259    16491    countproduct    VIEW     �  CREATE VIEW public.countproduct AS
 SELECT product.nameproduct,
    product.price,
    expenditureinvoice.dateei,
    expenditureinvoice.countei,
    receiptinvoice.dateri,
    receiptinvoice.countri,
    product.count
   FROM ((public.product
     LEFT JOIN public.expenditureinvoice ON ((expenditureinvoice.codeproductei = product.idproduct)))
     LEFT JOIN public.receiptinvoice ON ((receiptinvoice.codeproductri = product.idproduct)))
  WHERE (receiptinvoice.countri > expenditureinvoice.countei);
    DROP VIEW public.countproduct;
       public          postgres    false    205    207    207    207    203    203    203    203    205    205            �           0    0    TABLE countproduct    ACL     u   GRANT SELECT ON TABLE public.countproduct TO main_user;
GRANT SELECT ON TABLE public.countproduct TO secondary_user;
          public          postgres    false    208            �            1259    16428 $   expenditureinvoice_idexpenditure_seq    SEQUENCE     �   CREATE SEQUENCE public.expenditureinvoice_idexpenditure_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ;   DROP SEQUENCE public.expenditureinvoice_idexpenditure_seq;
       public          postgres    false    207            �           0    0 $   expenditureinvoice_idexpenditure_seq    SEQUENCE OWNED BY     m   ALTER SEQUENCE public.expenditureinvoice_idexpenditure_seq OWNED BY public.expenditureinvoice.idexpenditure;
          public          postgres    false    206            �            1259    16396    person    TABLE     �   CREATE TABLE public.person (
    idperson integer NOT NULL,
    firstname character varying(255) NOT NULL,
    secondname character varying(255) NOT NULL,
    patronymic character varying(255) NOT NULL
);
    DROP TABLE public.person;
       public         heap    postgres    false                        0    0    TABLE person    ACL     �   GRANT ALL ON TABLE public.person TO main_user;
GRANT ALL ON TABLE public.person TO secondary_user;
GRANT ALL ON TABLE public.person TO user_two;
          public          postgres    false    202            �            1259    16394    person_idperson_seq    SEQUENCE     �   CREATE SEQUENCE public.person_idperson_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.person_idperson_seq;
       public          postgres    false    202                       0    0    person_idperson_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.person_idperson_seq OWNED BY public.person.idperson;
          public          postgres    false    201            �            1259    16410    receiptinvoice_idreceipt_seq    SEQUENCE     �   CREATE SEQUENCE public.receiptinvoice_idreceipt_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.receiptinvoice_idreceipt_seq;
       public          postgres    false    205                       0    0    receiptinvoice_idreceipt_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public.receiptinvoice_idreceipt_seq OWNED BY public.receiptinvoice.idreceipt;
          public          postgres    false    204            P           2604    16433     expenditureinvoice idexpenditure    DEFAULT     �   ALTER TABLE ONLY public.expenditureinvoice ALTER COLUMN idexpenditure SET DEFAULT nextval('public.expenditureinvoice_idexpenditure_seq'::regclass);
 O   ALTER TABLE public.expenditureinvoice ALTER COLUMN idexpenditure DROP DEFAULT;
       public          postgres    false    207    206    207            N           2604    16399    person idperson    DEFAULT     r   ALTER TABLE ONLY public.person ALTER COLUMN idperson SET DEFAULT nextval('public.person_idperson_seq'::regclass);
 >   ALTER TABLE public.person ALTER COLUMN idperson DROP DEFAULT;
       public          postgres    false    202    201    202            O           2604    16415    receiptinvoice idreceipt    DEFAULT     �   ALTER TABLE ONLY public.receiptinvoice ALTER COLUMN idreceipt SET DEFAULT nextval('public.receiptinvoice_idreceipt_seq'::regclass);
 G   ALTER TABLE public.receiptinvoice ALTER COLUMN idreceipt DROP DEFAULT;
       public          postgres    false    205    204    205            �          0    16430    expenditureinvoice 
   TABLE DATA           i   COPY public.expenditureinvoice (idexpenditure, dateei, countei, codepersonei, codeproductei) FROM stdin;
    public          postgres    false    207   /s       �          0    16396    person 
   TABLE DATA           M   COPY public.person (idperson, firstname, secondname, patronymic) FROM stdin;
    public          postgres    false    202   xs       �          0    16405    product 
   TABLE DATA           T   COPY public.product (idproduct, codeproduct, nameproduct, price, count) FROM stdin;
    public          postgres    false    203   �s       �          0    16412    receiptinvoice 
   TABLE DATA           a   COPY public.receiptinvoice (idreceipt, dateri, countri, codepersonri, codeproductri) FROM stdin;
    public          postgres    false    205   ft                  0    0 $   expenditureinvoice_idexpenditure_seq    SEQUENCE SET     S   SELECT pg_catalog.setval('public.expenditureinvoice_idexpenditure_seq', 26, true);
          public          postgres    false    206                       0    0    person_idperson_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.person_idperson_seq', 18, true);
          public          postgres    false    201                       0    0    receiptinvoice_idreceipt_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public.receiptinvoice_idreceipt_seq', 31, true);
          public          postgres    false    204            Z           2606    16435 *   expenditureinvoice expenditureinvoice_pkey 
   CONSTRAINT     s   ALTER TABLE ONLY public.expenditureinvoice
    ADD CONSTRAINT expenditureinvoice_pkey PRIMARY KEY (idexpenditure);
 T   ALTER TABLE ONLY public.expenditureinvoice DROP CONSTRAINT expenditureinvoice_pkey;
       public            postgres    false    207            R           2606    16404    person person_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.person
    ADD CONSTRAINT person_pkey PRIMARY KEY (idperson);
 <   ALTER TABLE ONLY public.person DROP CONSTRAINT person_pkey;
       public            postgres    false    202            U           2606    16409    product product_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_pkey PRIMARY KEY (idproduct);
 >   ALTER TABLE ONLY public.product DROP CONSTRAINT product_pkey;
       public            postgres    false    203            X           2606    16417 "   receiptinvoice receiptinvoice_pkey 
   CONSTRAINT     g   ALTER TABLE ONLY public.receiptinvoice
    ADD CONSTRAINT receiptinvoice_pkey PRIMARY KEY (idreceipt);
 L   ALTER TABLE ONLY public.receiptinvoice DROP CONSTRAINT receiptinvoice_pkey;
       public            postgres    false    205            [           1259    16503    index_expenditureinvoice    INDEX     `   CREATE INDEX index_expenditureinvoice ON public.expenditureinvoice USING btree (idexpenditure);
 ,   DROP INDEX public.index_expenditureinvoice;
       public            postgres    false    207            S           1259    16460    index_product    INDEX     O   CREATE UNIQUE INDEX index_product ON public.product USING btree (codeproduct);
 !   DROP INDEX public.index_product;
       public            postgres    false    203            V           1259    16502    index_receiptinvoice    INDEX     T   CREATE INDEX index_receiptinvoice ON public.receiptinvoice USING btree (idreceipt);
 (   DROP INDEX public.index_receiptinvoice;
       public            postgres    false    205            a           2620    16497    expenditureinvoice productei    TRIGGER     �   CREATE TRIGGER productei AFTER INSERT OR DELETE OR UPDATE ON public.expenditureinvoice FOR EACH ROW EXECUTE FUNCTION public.add_to_log();
 5   DROP TRIGGER productei ON public.expenditureinvoice;
       public          postgres    false    207    234            `           2620    16499    receiptinvoice productri    TRIGGER     �   CREATE TRIGGER productri AFTER INSERT OR DELETE OR UPDATE ON public.receiptinvoice FOR EACH ROW EXECUTE FUNCTION public.add_to_log2();
 1   DROP TRIGGER productri ON public.receiptinvoice;
       public          postgres    false    205    235            \           2606    16418    receiptinvoice fk_person    FK CONSTRAINT     �   ALTER TABLE ONLY public.receiptinvoice
    ADD CONSTRAINT fk_person FOREIGN KEY (codepersonri) REFERENCES public.person(idperson) ON DELETE CASCADE;
 B   ALTER TABLE ONLY public.receiptinvoice DROP CONSTRAINT fk_person;
       public          postgres    false    205    2898    202            ^           2606    16436    expenditureinvoice fk_person    FK CONSTRAINT     �   ALTER TABLE ONLY public.expenditureinvoice
    ADD CONSTRAINT fk_person FOREIGN KEY (codepersonei) REFERENCES public.person(idperson) ON DELETE CASCADE;
 F   ALTER TABLE ONLY public.expenditureinvoice DROP CONSTRAINT fk_person;
       public          postgres    false    202    207    2898            ]           2606    16423    receiptinvoice fk_product    FK CONSTRAINT     �   ALTER TABLE ONLY public.receiptinvoice
    ADD CONSTRAINT fk_product FOREIGN KEY (codeproductri) REFERENCES public.product(idproduct) ON DELETE CASCADE;
 C   ALTER TABLE ONLY public.receiptinvoice DROP CONSTRAINT fk_product;
       public          postgres    false    205    203    2901            _           2606    16441    expenditureinvoice fk_product    FK CONSTRAINT     �   ALTER TABLE ONLY public.expenditureinvoice
    ADD CONSTRAINT fk_product FOREIGN KEY (codeproductei) REFERENCES public.product(idproduct) ON DELETE CASCADE;
 G   ALTER TABLE ONLY public.expenditureinvoice DROP CONSTRAINT fk_product;
       public          postgres    false    207    2901    203            �           826    16486     DEFAULT PRIVILEGES FOR SEQUENCES    DEFAULT ACL     ?  ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public REVOKE ALL ON SEQUENCES  FROM postgres;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT SELECT,USAGE ON SEQUENCES  TO main_user;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT SELECT,USAGE ON SEQUENCES  TO secondary_user;
          public          postgres    false            �           826    16487     DEFAULT PRIVILEGES FOR FUNCTIONS    DEFAULT ACL     �  ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public REVOKE ALL ON FUNCTIONS  FROM PUBLIC;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public REVOKE ALL ON FUNCTIONS  FROM postgres;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON FUNCTIONS  TO main_user;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON FUNCTIONS  TO secondary_user;
          public          postgres    false            �           826    16485    DEFAULT PRIVILEGES FOR TABLES    DEFAULT ACL     *  ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public REVOKE ALL ON TABLES  FROM postgres;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT SELECT ON TABLES  TO main_user;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT SELECT ON TABLES  TO secondary_user;
          public          postgres    false            �   9   x�=��� �w�(I�0���#DQs�Å�d����?13���m�̷�����      �   =   x�34�0��.컰�;9/,����.6 �6q^�a��&���\1z\\\ �V!�      �   �   x�E���@D��*� @����F(Ɵ $w@Z��;>r0��̛���gሄ���j�D���5[���"�t��`ʹ�-��O�b���=y�Om�3��̸����_j�**���!3�rmY\��-��gG�m��JM�      �   4   x�ɹ  �:�%�m�3����g�fʩ"C݂��d�1>�%�����     