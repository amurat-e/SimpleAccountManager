-- Table: public.passwords

-- DROP TABLE public.passwords;

CREATE TABLE public.passwords
(
    psw_id integer NOT NULL DEFAULT nextval('passwords_psw_id_seq'::regclass),
    act_id integer NOT NULL,
    psw_data bytea NOT NULL,
    CONSTRAINT passwords_pkey PRIMARY KEY (psw_id, act_id),
    CONSTRAINT passwords_fk1 FOREIGN KEY (act_id)
        REFERENCES public.accounts (act_id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
)

TABLESPACE pg_default;

ALTER TABLE public.passwords
    OWNER to postgres;

GRANT DELETE, INSERT, SELECT, UPDATE ON TABLE public.passwords TO generic_role WITH GRANT OPTION;

GRANT ALL ON TABLE public.passwords TO postgres;

COMMENT ON TABLE public.passwords
    IS 'Contains passwords for accounts table';

COMMENT ON CONSTRAINT passwords_fk1 ON public.passwords
    IS 'act id from accounts table';