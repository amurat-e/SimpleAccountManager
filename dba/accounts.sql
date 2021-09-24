-- Table: public.accounts

-- DROP TABLE public.accounts;

CREATE TABLE public.accounts
(
    act_id integer NOT NULL DEFAULT nextval('account_act_id_seq'::regclass),
    act_name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    act_type integer NOT NULL,
    act_timestamp timestamp with time zone NOT NULL,
    act_stat integer NOT NULL,
    act_username character varying(100) COLLATE pg_catalog."default",
    act_url character varying(1000) COLLATE pg_catalog."default",
    act_email character varying(1000) COLLATE pg_catalog."default",
    act_exp character varying(2000) COLLATE pg_catalog."default",
    CONSTRAINT account_pk PRIMARY KEY (act_id)
)

TABLESPACE pg_default;

ALTER TABLE public.accounts
    OWNER to postgres;

GRANT DELETE, INSERT, SELECT, UPDATE ON TABLE public.accounts TO generic_role WITH GRANT OPTION;

GRANT ALL ON TABLE public.accounts TO postgres;

COMMENT ON TABLE public.accounts
    IS 'Account info';