--
-- PostgreSQL database dump
--

-- Dumped from database version 12.3
-- Dumped by pg_dump version 12.3

-- Started on 2020-12-23 20:05:57

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
-- TOC entry 2839 (class 0 OID 0)
-- Dependencies: 205
-- Name: events_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.events_id_seq OWNED BY public.events.id;


--
-- TOC entry 2702 (class 2604 OID 17490)
-- Name: events id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.events ALTER COLUMN id SET DEFAULT nextval('public.events_id_seq'::regclass);


--
-- TOC entry 2833 (class 0 OID 17487)
-- Dependencies: 206
-- Data for Name: events; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.events (id, event_name, event_date, location, division, fighter_1, fighter_2, fighter_1_votes, fighter_2_votes, fighter_1_odds, fighter_2_odds, fight_order) FROM stdin;
25	Do Not Delete	2000-12-22 18:30:31	DO NOT DELETE	1	DO NOT DELETE	DO NOT DELETE	0	0	1	1	1
26	DO NOT DELETE	1999-12-22 18:30:31	DO NOT DELETE	1	DO NOT DELETE	DO NOT DELETE	0	0	1	1	1
22	UFC 256: Figueiredo vs. Moreno	2020-12-12 22:00:00	UFC APEX, Las Vegas, NY	4	Moicano	Fiziev	8	14	120	-140	3
21	UFC 256: Figueiredo vs. Moreno	2020-12-12 22:00:00	UFC APEX, Las Vegas, NY	4	Ferguson	Oliveira	8	9	-160	140	2
30	UFC Fight Night: Thompson vs. Neal	2020-12-19 16:00:00	UFC APEX, Las Vegas, NV	2	Moraes	Font	3	4	100	-100	4
24	UFC 256: Figueiredo vs. Moreno	2020-12-12 22:00:00	UFC APEX, Las Vegas, NY	8	Dos-Santos	Gane	12	11	350	-430	5
29	UFC Fight Night: Thompson vs. Neal	2020-12-19 16:00:00	UFC APEX, Las Vegas, NV	5	Pereira	Williams	5	16	-200	100	3
23	UFC 256: Figueiredo vs. Moreno	2020-12-12 22:00:00	UFC APEX, Las Vegas, NY	6	Souza	Holland	12	13	141	-169	4
27	UFC Fight Night: Thompson vs. Neal	2020-12-19 16:00:00	UFC APEX, Las Vegas, NV	5	Thompson	Neal	14	2	-100	200	1
28	UFC Fight Night: Thompson vs. Neal	2020-12-19 16:00:00	UFC APEX, Las Vegas, NV	2	Aldo	Vera	5	3	-150	100	2
31	UFC Fight Night: Thompson vs. Neal	2020-12-19 16:00:00	UFC APEX, Las Vegas, NV	8	Tybura	Hardy	12	3	200	-100	5
20	UFC 256: Figueiredo vs. Moreno	2020-12-12 22:00:00	UFC APEX, Las Vegas, NY	1	Figueiredo	Moreno	7	15	-300	250	1
\.


--
-- TOC entry 2840 (class 0 OID 0)
-- Dependencies: 205
-- Name: events_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.events_id_seq', 31, true);


--
-- TOC entry 2704 (class 2606 OID 17495)
-- Name: events events_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.events
    ADD CONSTRAINT events_pkey PRIMARY KEY (id);


--
-- TOC entry 2705 (class 2606 OID 17496)
-- Name: events events_division_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.events
    ADD CONSTRAINT events_division_fkey FOREIGN KEY (division) REFERENCES public.divisions(id);


-- Completed on 2020-12-23 20:05:57

--
-- PostgreSQL database dump complete
--

