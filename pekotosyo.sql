--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: books; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE books (
    book_id character varying(8) NOT NULL,
    book_name character varying(255) NOT NULL,
    book_genre character varying(255) NOT NULL
);


ALTER TABLE public.books OWNER TO postgres;

--
-- Name: borrowbook; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE borrowbook (
    keyid integer NOT NULL,
    user_id character varying(8),
    book_id character varying(8),
    frag integer NOT NULL,
    deadline date NOT NULL
);


ALTER TABLE public.borrowbook OWNER TO postgres;

--
-- Name: borrowbook_keyid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE borrowbook_keyid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.borrowbook_keyid_seq OWNER TO postgres;

--
-- Name: borrowbook_keyid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE borrowbook_keyid_seq OWNED BY borrowbook.keyid;


--
-- Name: cardhistory; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE cardhistory (
    cardhistory_id integer NOT NULL,
    userid character varying(8),
    history_date date NOT NULL,
    chargemoney integer NOT NULL
);


ALTER TABLE public.cardhistory OWNER TO postgres;

--
-- Name: cardhistory_cardhistory_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE cardhistory_cardhistory_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cardhistory_cardhistory_id_seq OWNER TO postgres;

--
-- Name: cardhistory_cardhistory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE cardhistory_cardhistory_id_seq OWNED BY cardhistory.cardhistory_id;


--
-- Name: cardinfo; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE cardinfo (
    cardinfo_id integer NOT NULL,
    user_id character varying(8),
    card_number character varying(16),
    card_key character varying(3),
    card_date integer,
    card_name character varying(10),
    user_money integer NOT NULL
);


ALTER TABLE public.cardinfo OWNER TO postgres;

--
-- Name: cardinfo_cardinfo_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE cardinfo_cardinfo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cardinfo_cardinfo_id_seq OWNER TO postgres;

--
-- Name: cardinfo_cardinfo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE cardinfo_cardinfo_id_seq OWNED BY cardinfo.cardinfo_id;


--
-- Name: reserve; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE reserve (
    reserve_id integer NOT NULL,
    user_id character varying(8),
    reserve_date date,
    item character varying(255) NOT NULL
);


ALTER TABLE public.reserve OWNER TO postgres;

--
-- Name: reserve_reserve_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE reserve_reserve_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.reserve_reserve_id_seq OWNER TO postgres;

--
-- Name: reserve_reserve_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE reserve_reserve_id_seq OWNED BY reserve.reserve_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE users (
    user_id character varying(8) NOT NULL,
    password character varying(8) NOT NULL,
    user_name character varying(8) NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: keyid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY borrowbook ALTER COLUMN keyid SET DEFAULT nextval('borrowbook_keyid_seq'::regclass);


--
-- Name: cardhistory_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY cardhistory ALTER COLUMN cardhistory_id SET DEFAULT nextval('cardhistory_cardhistory_id_seq'::regclass);


--
-- Name: cardinfo_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY cardinfo ALTER COLUMN cardinfo_id SET DEFAULT nextval('cardinfo_cardinfo_id_seq'::regclass);


--
-- Name: reserve_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY reserve ALTER COLUMN reserve_id SET DEFAULT nextval('reserve_reserve_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY alembic_version (version_num) FROM stdin;
f44b4dd9d9ab
\.


--
-- Data for Name: books; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY books (book_id, book_name, book_genre) FROM stdin;
0000001	精霊の守り人	ファンタジー
0000002	月の影　影の海	ファンタジー
0000003	空色勾玉	ファンタジー
0000004	獣の奏者　闘蛇編	ファンタジー
0000005	霧のむこうのふしぎな町	ファンタジー
0000006	銀河英雄伝説列伝1 晴れあがる銀河	SF
0000007	彼女は一人で歩くのか？ Does She Walk Alone？	SF
0000008	るん（笑）	SF
0000009	復活の日	SF
0000010	空の中	SF
0000011	ぼぎわんが、来る	ホラー
0000012	ホーンテッド・キャンパス	ホラー
0000013	ずうのめ人形	ホラー
0000014	ゴーストハント1 旧校舎怪談	ホラー
0000015	怪談喫茶ニライカナイ	ホラー
0000016	すべてがFになる	サスペンス
0000017	『アリス・ミラー城』殺人事件	サスペンス
0000018	屍人荘の殺人	サスペンス
0000019	ジョーカー・ゲーム	サスペンス
0000020	悪魔の手毬唄	サスペンス
\.


--
-- Data for Name: borrowbook; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY borrowbook (keyid, user_id, book_id, frag, deadline) FROM stdin;
\.


--
-- Name: borrowbook_keyid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('borrowbook_keyid_seq', 1, false);


--
-- Data for Name: cardhistory; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY cardhistory (cardhistory_id, userid, history_date, chargemoney) FROM stdin;
\.


--
-- Name: cardhistory_cardhistory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('cardhistory_cardhistory_id_seq', 1, false);


--
-- Data for Name: cardinfo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY cardinfo (cardinfo_id, user_id, card_number, card_key, card_date, card_name, user_money) FROM stdin;
\.


--
-- Name: cardinfo_cardinfo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('cardinfo_cardinfo_id_seq', 1, false);


--
-- Data for Name: reserve; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY reserve (reserve_id, user_id, reserve_date, item) FROM stdin;
\.


--
-- Name: reserve_reserve_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('reserve_reserve_id_seq', 1, false);


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY users (user_id, password, user_name) FROM stdin;
00000001	pass01	Aoyama
00000002	pass02	Kakita
00000003	pass03	Saito
00000004	pass04	Tanaka
00000005	pass05	Narita
00000006	pass06	Harui
00000007	pass07	Makabe
00000008	pass08	Yanagi
00000009	pass09	Rakuyama
00000010	pass10	Watanabe
\.


--
-- Name: alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: books_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY books
    ADD CONSTRAINT books_pkey PRIMARY KEY (book_id);


--
-- Name: borrowbook_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY borrowbook
    ADD CONSTRAINT borrowbook_pkey PRIMARY KEY (keyid);


--
-- Name: cardhistory_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY cardhistory
    ADD CONSTRAINT cardhistory_pkey PRIMARY KEY (cardhistory_id);


--
-- Name: cardinfo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY cardinfo
    ADD CONSTRAINT cardinfo_pkey PRIMARY KEY (cardinfo_id);


--
-- Name: reserve_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY reserve
    ADD CONSTRAINT reserve_pkey PRIMARY KEY (reserve_id);


--
-- Name: users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: borrowbook_book_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY borrowbook
    ADD CONSTRAINT borrowbook_book_id_fkey FOREIGN KEY (book_id) REFERENCES books(book_id);


--
-- Name: borrowbook_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY borrowbook
    ADD CONSTRAINT borrowbook_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(user_id);


--
-- Name: cardhistory_userid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY cardhistory
    ADD CONSTRAINT cardhistory_userid_fkey FOREIGN KEY (userid) REFERENCES users(user_id);


--
-- Name: cardinfo_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY cardinfo
    ADD CONSTRAINT cardinfo_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(user_id);


--
-- Name: reserve_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY reserve
    ADD CONSTRAINT reserve_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(user_id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

