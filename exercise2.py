-- This script was generated by the ERD tool in pgAdmin 4.
-- Please log an issue at https://redmine.postgresql.org/projects/pgadmin4/issues/new if you find any bugs, including reproduction steps.
BEGIN;


CREATE TABLE IF NOT EXISTS public.teams
(
    product_id bigint NOT NULL,
    product_owner character varying,
    backend_developer character varying,
    frontend_developer character varying,
    data_engineer character varying,
    team_num bigint NOT NULL,
    PRIMARY KEY (team_num),
    UNIQUE (product_id)
);

CREATE TABLE IF NOT EXISTS public.products
(
    product_id bigint NOT NULL,
    product_name character varying,
    PRIMARY KEY (product_id),
    UNIQUE (product_id)
);

CREATE TABLE IF NOT EXISTS public.customers
(
    customer_id bigint NOT NULL,
    customer_name character varying,
    customer_adress character varying,
    product_id bigint,
    PRIMARY KEY (customer_id)
);

CREATE TABLE IF NOT EXISTS public.domens
(
    domen_name character varying NOT NULL,
    customer_id bigint,
    PRIMARY KEY (domen_name)
);

CREATE TABLE IF NOT EXISTS public.employees
(
    name character varying,
    forname character varying,
    team_num bigint,
    employee_num bigint NOT NULL,
    PRIMARY KEY (employee_num)
);

ALTER TABLE IF EXISTS public.teams
    ADD CONSTRAINT product FOREIGN KEY (product_id)
    REFERENCES public.products (product_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.customers
    ADD CONSTRAINT products FOREIGN KEY (product_id)
    REFERENCES public.products (product_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.domens
    ADD CONSTRAINT customer FOREIGN KEY (customer_id)
    REFERENCES public.customers (customer_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.employees
    ADD FOREIGN KEY (team_num)
    REFERENCES public.teams (team_num) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

END;