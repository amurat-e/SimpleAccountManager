-- SEQUENCE: public.passwords_psw_id_seq

-- DROP SEQUENCE public.passwords_psw_id_seq;

CREATE SEQUENCE public.passwords_psw_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.passwords_psw_id_seq
    OWNER TO postgres;

GRANT ALL ON SEQUENCE public.passwords_psw_id_seq TO generic_role WITH GRANT OPTION;

GRANT ALL ON SEQUENCE public.passwords_psw_id_seq TO postgres;