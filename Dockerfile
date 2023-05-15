FROM mambaorg/micromamba
COPY --chown=$MAMBA_USER:$MAMBA_USER test/requirements.*.txt /tmp/
RUN micromamba install -y -n base -f /tmp/requirements.dev.txt  /tmp/requirements.prod.txt && \
    micromamba clean --all --yes && \
    rm /tmp/requirements.dev.txt  /tmp/requirements.prod.txt
