FROM mambaorg/micromamba:1.4.2
COPY --chown=$MAMBA_USER:$MAMBA_USER requirements.*.txt /tmp/
RUN micromamba install -y -c conda-forge -n base -f /tmp/requirements.dev.txt -f /tmp/requirements.prod.txt && \
    micromamba clean --all --yes && \
    rm /tmp/requirements.dev.txt  /tmp/requirements.prod.txt
