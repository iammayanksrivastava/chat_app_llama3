def set_global_exception_handler(f):
    import sys

    script_runner = sys.modules["streamlit.runtime.scriptrunner.script_runner"]
    script_runner.handle_uncaught_app_exception.__code__ = f.__code__


def exception_handler(e):
    # Custom error handling
    st.image("https://media1.tenor.com/m/t7_iTN0iYekAAAAd/sad-sad-cat.gif")
    st.error(f"Oops, something funny happened with a {type(e).__name__}", icon="😿")
