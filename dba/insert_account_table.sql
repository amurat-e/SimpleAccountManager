-- FUNCTION: public.insert_account_table(text, integer, text, text, text, text, text, text)

-- DROP FUNCTION public.insert_account_table(text, integer, text, text, text, text, text, text);

CREATE OR REPLACE FUNCTION public.insert_account_table(
	actname text DEFAULT NULL::text,
	acttype integer DEFAULT 1,
	actusrn text DEFAULT NULL::text,
	acturl text DEFAULT NULL::text,
	acteml text DEFAULT NULL::text,
	actexpl text DEFAULT NULL::text,
	actpswd text DEFAULT NULL::text,
	pswdkey text DEFAULT NULL::text)
    RETURNS text
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
AS $BODY$
DECLARE 
actid integer;
BEGIN
	INSERT INTO public.accounts(
	act_id, act_name, act_type, act_timestamp, act_stat, act_username, act_url, act_email, act_exp)
	VALUES (DEFAULT, actname, acttype, (SELECT CURRENT_TIMESTAMP), 1, actusrn, acturl, acteml,actexpl);
	
	SELECT act_id INTO STRICT actid FROM public.accounts where act_name = actname;
	
	INSERT INTO public.passwords(psw_id, act_id, psw_data)
	VALUES (DEFAULT, actid, (pgp_sym_encrypt(actpswd,pswdkey)));
	
			RETURN 'Ok...';
		EXCEPTION
			WHEN NO_DATA_FOUND THEN
				RAISE INFO 'Error Name:%',SQLERRM;
        		RAISE INFO 'Error State:%', SQLSTATE;
        		RETURN username||' Kullanıcısı Bulunamadı. ['||SQLSTATE||':'||SQLERRM||']';
			WHEN OTHERS THEN
				RAISE INFO 'Error Name:%',SQLERRM;
        		RAISE INFO 'Error State:%', SQLSTATE;
        		RETURN SQLSTATE||':'||SQLERRM;
	
END;
$BODY$;

ALTER FUNCTION public.insert_account_table(text, integer, text, text, text, text, text, text)
    OWNER TO postgres;

GRANT EXECUTE ON FUNCTION public.insert_account_table(text, integer, text, text, text, text, text, text) TO PUBLIC;

GRANT EXECUTE ON FUNCTION public.insert_account_table(text, integer, text, text, text, text, text, text) TO generic_role WITH GRANT OPTION;

GRANT EXECUTE ON FUNCTION public.insert_account_table(text, integer, text, text, text, text, text, text) TO postgres;

