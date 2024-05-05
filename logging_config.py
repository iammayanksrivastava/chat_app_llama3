import logging


def configure_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s %(asctime)s %(name)s:%(message)s",
        force=True,
    )

    # Disable Streamlit's internal logging configuration
    import streamlit as st

    st.logger.get_logger = logging.getLogger
    st.logger.setup_formatter = None
    st.logger.update_formatter = lambda *a, k: None
    st.logger.set_log_level = lambda *a, k: None
