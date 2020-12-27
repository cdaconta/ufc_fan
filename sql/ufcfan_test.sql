--
-- PostgreSQL database dump
--

-- Dumped from database version 12.3
-- Dumped by pg_dump version 12.3

-- Started on 2020-12-27 10:28:08

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 202 (class 1259 OID 17469)
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 17476)
-- Name: divisions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.divisions (
    id integer NOT NULL,
    name character varying,
    weight integer
);


ALTER TABLE public.divisions OWNER TO postgres;

--
-- TOC entry 203 (class 1259 OID 17474)
-- Name: divisions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.divisions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.divisions_id_seq OWNER TO postgres;

--
-- TOC entry 2857 (class 0 OID 0)
-- Dependencies: 203
-- Name: divisions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.divisions_id_seq OWNED BY public.divisions.id;


--
-- TOC entry 206 (class 1259 OID 17487)
-- Name: events; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.events (
    id integer NOT NULL,
    event_name character varying,
    event_date timestamp without time zone,
    location character varying,
    division integer,
    fighter_1 character varying,
    fighter_2 character varying,
    fighter_1_votes integer,
    fighter_2_votes integer,
    fighter_1_odds integer,
    fighter_2_odds integer,
    fight_order integer
);


ALTER TABLE public.events OWNER TO postgres;

--
-- TOC entry 205 (class 1259 OID 17485)
-- Name: events_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.events_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.events_id_seq OWNER TO postgres;

--
-- TOC entry 2858 (class 0 OID 0)
-- Dependencies: 205
-- Name: events_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.events_id_seq OWNED BY public.events.id;


--
-- TOC entry 208 (class 1259 OID 17503)
-- Name: fighters; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fighters (
    id integer NOT NULL,
    first_name character varying,
    last_name character varying,
    age integer,
    height double precision,
    weight double precision,
    arm_reach double precision,
    leg_reach double precision,
    sex character varying(1),
    win integer,
    loss integer,
    draw integer,
    division integer,
    rank integer
);


ALTER TABLE public.fighters OWNER TO postgres;

--
-- TOC entry 207 (class 1259 OID 17501)
-- Name: fighters_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fighters_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fighters_id_seq OWNER TO postgres;

--
-- TOC entry 2859 (class 0 OID 0)
-- Dependencies: 207
-- Name: fighters_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fighters_id_seq OWNED BY public.fighters.id;


--
-- TOC entry 2706 (class 2604 OID 17479)
-- Name: divisions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.divisions ALTER COLUMN id SET DEFAULT nextval('public.divisions_id_seq'::regclass);


--
-- TOC entry 2707 (class 2604 OID 17490)
-- Name: events id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.events ALTER COLUMN id SET DEFAULT nextval('public.events_id_seq'::regclass);


--
-- TOC entry 2708 (class 2604 OID 17506)
-- Name: fighters id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fighters ALTER COLUMN id SET DEFAULT nextval('public.fighters_id_seq'::regclass);


--
-- TOC entry 2845 (class 0 OID 17469)
-- Dependencies: 202
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
f23e9899c570
\.


--
-- TOC entry 2847 (class 0 OID 17476)
-- Dependencies: 204
-- Data for Name: divisions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.divisions (id, name, weight) FROM stdin;
\.


--
-- TOC entry 2849 (class 0 OID 17487)
-- Dependencies: 206
-- Data for Name: events; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.events (id, event_name, event_date, location, division, fighter_1, fighter_2, fighter_1_votes, fighter_2_votes, fighter_1_odds, fighter_2_odds, fight_order) FROM stdin;
\.


--
-- TOC entry 2851 (class 0 OID 17503)
-- Dependencies: 208
-- Data for Name: fighters; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fighters (id, first_name, last_name, age, height, weight, arm_reach, leg_reach, sex, win, loss, draw, division, rank) FROM stdin;
\.


--
-- TOC entry 2860 (class 0 OID 0)
-- Dependencies: 203
-- Name: divisions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.divisions_id_seq', 187, true);


--
-- TOC entry 2861 (class 0 OID 0)
-- Dependencies: 205
-- Name: events_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.events_id_seq', 39, true);


--
-- TOC entry 2862 (class 0 OID 0)
-- Dependencies: 207
-- Name: fighters_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fighters_id_seq', 909, true);


--
-- TOC entry 2710 (class 2606 OID 17473)
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- TOC entry 2712 (class 2606 OID 17484)
-- Name: divisions divisions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.divisions
    ADD CONSTRAINT divisions_pkey PRIMARY KEY (id);


--
-- TOC entry 2714 (class 2606 OID 17495)
-- Name: events events_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.events
    ADD CONSTRAINT events_pkey PRIMARY KEY (id);


--
-- TOC entry 2716 (class 2606 OID 17511)
-- Name: fighters fighters_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fighters
    ADD CONSTRAINT fighters_pkey PRIMARY KEY (id);


--
-- TOC entry 2717 (class 2606 OID 17496)
-- Name: events events_division_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.events
    ADD CONSTRAINT events_division_fkey FOREIGN KEY (division) REFERENCES public.divisions(id);


--
-- TOC entry 2718 (class 2606 OID 17512)
-- Name: fighters fighters_division_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fighters
    ADD CONSTRAINT fighters_division_fkey FOREIGN KEY (division) REFERENCES public.divisions(id);


-- Completed on 2020-12-27 10:28:08

--
-- PostgreSQL database dump complete
--

