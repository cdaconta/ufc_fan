--
-- PostgreSQL database dump
--

-- Dumped from database version 12.3
-- Dumped by pg_dump version 12.3

-- Started on 2020-12-23 20:20:59

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
-- TOC entry 2839 (class 0 OID 0)
-- Dependencies: 207
-- Name: fighters_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fighters_id_seq OWNED BY public.fighters.id;


--
-- TOC entry 2702 (class 2604 OID 17506)
-- Name: fighters id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fighters ALTER COLUMN id SET DEFAULT nextval('public.fighters_id_seq'::regclass);


--
-- TOC entry 2833 (class 0 OID 17503)
-- Dependencies: 208
-- Data for Name: fighters; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fighters (id, first_name, last_name, age, height, weight, arm_reach, leg_reach, sex, win, loss, draw, division, rank) FROM stdin;
71	Joseph	Benavidez	35	64	126	65	36	M	28	7	0	1	1
73	Askar	Askarov	27	66	125	67	36	M	11	0	1	1	3
74	Alex	Perez	28	66	125	65.5	38	M	24	5	0	1	4
75	Alexandre	Pantoja	30	65	125	67	36.5	M	22	5	0	1	5
76	Petr	Yan	27	67.5	135	67	38	M	15	1	0	2	0
77	Aljamain	Sterling	30	67	136	71	39	M	19	3	0	2	1
78	Cory	Sandhagen	28	71	135	70	40	M	13	2	0	2	2
79	Marlon	Moraes	32	66	135	67	37	M	23	7	1	2	3
80	Cody	Garbrandt	28	68	135	65.5	38	M	12	3	0	2	4
81	Frankie	Edgar	38	66	135	68	37.5	M	23	8	1	2	5
82	Alexander	Volkanovski	31	66	145	71.5	36	M	22	1	0	3	0
83	Max	Holloway	28	71	146	69	42	M	21	6	0	3	1
84	Brian	Ortega	29	68	145	69	39	M	15	1	0	3	2
85	Zabit	Magomedsharipov	29	73	145	73	42	M	18	1	0	3	3
86	Yair	Rodriguez	27	71	145	71	41.5	M	13	2	0	3	4
87	Chan	Sung Jung	33	67	145	72	38.5	M	16	6	0	3	5
88	Khabib	Nurmagomedov	32	70	155	70	40	M	28	0	0	4	0
89	Justin	Gaethje	31	71	155	70	40	M	22	3	0	4	1
90	Dustin	Poirier	31	69	155	72	40.5	M	26	6	0	4	2
91	Tony	Ferguson	36	71	155	76.5	40.5	M	26	5	0	4	3
92	Conor	McGregor	32	69	145	74	40	M	22	4	0	4	4
93	Dan	Hooker	30	72	145	75	42.5	M	20	9	0	4	5
94	Kamaru	Usman	33	72	170	76	41	M	17	1	0	5	0
95	Colby	Covington	32	71	170	72	41	M	15	2	0	5	1
96	Gilbert	Burns	33	70	155	71	40	M	19	3	0	5	2
97	Leon	Edwards	28	72	170	74	43	M	18	3	0	5	3
98	Jorge	Masvidal	35	71	156	74	39.5	M	35	14	0	5	4
100	Israel	Adesanya	31	76	185	80	44.5	M	19	0	0	6	0
101	Robert	Whittaker	29	72	185	73.5	43	M	22	5	0	6	1
102	Paulo	Costa	29	73	185	72	39.5	M	13	0	0	6	2
103	Jared	Cannonier	36	71	205	77.5	41.5	M	13	4	0	6	3
104	Jack	Hermansson	32	73	186	77.5	46.5	M	21	5	0	6	4
105	Yoel	Romero	43	72	185	73.5	42	M	13	5	0	6	5
106	Jan	Blachowicz	37	74	216	78	44	M	27	8	0	7	0
107	Glover	Teixeira	41	74	205	76	42.5	M	31	7	0	7	1
108	Thiago	Santos	36	74	205	76	42.5	M	21	8	0	7	2
109	Dominick	Reyes	30	76	205	77	43.5	M	12	1	0	7	3
110	Aleksandar	Rakic	28	76	205	78	46	M	13	2	0	7	4
111	Jiri	Prochazka	27	75	205	80	45	M	27	3	1	7	5
112	Stipe	Miocic	37	77	240	80	39	M	20	3	0	8	0
113	Francis	Ngannou	33	76	250	83	44.5	M	15	3	0	8	1
114	Curtis	Blaydes	29	76	265	80	46	M	14	2	0	8	2
115	Jairzinho	Rozenstruik	32	76	242	78	41	M	11	1	0	8	3
116	Derrick	Lewis	35	75	260	79	43.5	M	23	7	0	8	4
117	Alistair	Overeem	40	76	260	80	44.5	M	47	18	0	8	5
118	Weili	Zhang	30	64	115	63	36	F	21	1	0	9	0
119	Rose	Namajunas	28	65	115	65	39.5	F	10	4	0	9	1
120	Joanna	Jedrzejczyk	32	66	115	65.5	35	F	16	4	0	9	2
121	Yan	Xiaonan	31	65	115	63	37	F	13	1	0	9	3
122	Carla	Esparza	32	61	115	63	35	F	18	6	0	9	4
123	Nina	Ansaroff	34	65	115	64	39	F	10	6	0	9	5
124	Valentina	Shevchenko	32	65	125	67	38	F	19	3	0	10	0
125	Jessica	Andrade	29	61.5	135	62	35	F	21	8	0	10	1
126	Katlyn	Chookagian	31	69	125	68	42	F	14	4	0	10	2
127	Jennifer	Maia	32	64	125	64	38	F	18	6	1	10	3
128	Cynthia	Calvillo	33	64	125	64	37	F	9	1	1	10	4
129	Lauren	Murphy	37	65	135	67	38	F	13	4	0	10	5
130	Amanda	Nunes	32	68	135	69	41	F	20	4	0	11	0
131	Germaine	de Randamie	36	69	135	71	41	F	10	4	0	11	1
132	Holly	Holm	39	68	135	69	38	F	14	5	0	11	2
133	Aspen	Ladd	25	66	135	66	38.5	F	9	1	0	11	3
134	Raquel	Pennington	31	67	135	67.5	37	F	11	9	0	11	4
135	Irene	Aldana	32	69	135	68.5	38.5	F	12	6	0	11	5
136	Amanda	Nunes	32	68	135	69	41	F	20	4	0	12	0
137	Felicia	Spencer	29	66	145	68	40	F	8	2	0	12	1
138	Megan	Anderson	31	72	145	68	40	F	8	2	0	12	2
139			0	0	0	0	0	F	0	0	0	12	3
140			0	0	0	0	0	F	0	0	0	12	4
141			0	0	0	0	0	F	0	0	0	12	5
70	Deiveson	Figueiredo	32	65	125	68	38	M	19	1	1	1	0
72	Brandon	Moreno	26	67	125	70	38	M	17	5	2	1	2
99	Stephen	Thompson	37	72	170	75	42	M	16	4	1	5	5
\.


--
-- TOC entry 2840 (class 0 OID 0)
-- Dependencies: 207
-- Name: fighters_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fighters_id_seq', 141, true);


--
-- TOC entry 2704 (class 2606 OID 17511)
-- Name: fighters fighters_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fighters
    ADD CONSTRAINT fighters_pkey PRIMARY KEY (id);


--
-- TOC entry 2705 (class 2606 OID 17512)
-- Name: fighters fighters_division_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fighters
    ADD CONSTRAINT fighters_division_fkey FOREIGN KEY (division) REFERENCES public.divisions(id);


-- Completed on 2020-12-23 20:20:59

--
-- PostgreSQL database dump complete
--

