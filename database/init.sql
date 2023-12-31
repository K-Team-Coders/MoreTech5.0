PGDMP     "    7    	        	    {         
   moretechdb    14.7    14.7     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    40990 
   moretechdb    DATABASE     g   CREATE DATABASE moretechdb WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Russian_Russia.1251';
    DROP DATABASE moretechdb;
                postgres    false            �            1259    40992    queue    TABLE     �   CREATE TABLE public.queue (
    id bigint NOT NULL,
    service_time double precision,
    service text,
    "timestamp" timestamp without time zone NOT NULL,
    address text,
    latitude double precision,
    longitude double precision
);
    DROP TABLE public.queue;
       public         heap    postgres    false            �            1259    40991    queue_id_seq    SEQUENCE     u   CREATE SEQUENCE public.queue_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.queue_id_seq;
       public          postgres    false    210            �           0    0    queue_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.queue_id_seq OWNED BY public.queue.id;
          public          postgres    false    209            \           2604    40995    queue id    DEFAULT     d   ALTER TABLE ONLY public.queue ALTER COLUMN id SET DEFAULT nextval('public.queue_id_seq'::regclass);
 7   ALTER TABLE public.queue ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    210    209    210            �          0    40992    queue 
   TABLE DATA           e   COPY public.queue (id, service_time, service, "timestamp", address, latitude, longitude) FROM stdin;
    public          postgres    false    210   �
       �           0    0    queue_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.queue_id_seq', 42932, true);
          public          postgres    false    209            ^           2606    40999    queue queue_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public.queue
    ADD CONSTRAINT queue_pkey PRIMARY KEY (id, "timestamp");
 :   ALTER TABLE ONLY public.queue DROP CONSTRAINT queue_pkey;
       public            postgres    false    210    210            �      x������ � �     