-- FUNCTION: public.update_account_table(integer, text, integer, text, text, text, text, text, text)

-- DROP FUNCTION public.update_account_table(integer, text, integer, text, text, text, text, text, text);

CREATE OR REPLACE FUNCTION public.update_account_table(
	actid integer,
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
pswid integer;
BEGIN
	UPDATE public.accounts SET
	act_name = actname, 
	act_type = acttype,
	act_timestamp = (SELECT CURRENT_TIMESTAMP), 
	act_username = actusrn, 
	act_url = acturl,
	act_email = acteml, 
	act_exp = actexpl
	WHERE act_id = actid;
	
		SELECT psw_id INTO STRICT pswid FROM public.passwords where act_id = actid;
	
			UPDATE public.passwords SET
			psw_data = (pgp_sym_encrypt(actpswd,pswdkey))
			WHERE psw_id = pswid AND act_id = actid;
			
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

ALTER FUNCTION public.update_account_table(integer, text, integer, text, text, text, text, text, text)
    OWNER TO postgres;

GRANT EXECUTE ON FUNCTION public.update_account_table(integer, text, integer, text, text, text, text, text, text) TO PUBLIC;

GRANT EXECUTE ON FUNCTION public.update_account_table(integer, text, integer, text, text, text, text, text, text) TO generic_role WITH GRANT OPTION;

GRANT EXECUTE ON FUNCTION public.update_account_table(integer, text, integer, text, text, text, text, text, text) TO postgres;

