FROM {{base_image}}

WORKDIR "/root"

COPY "ncurses.control" "libncurses/DEBIAN/control"

RUN sed -i "s/{{version}}/{{ncurses_version}}/g"  \
        "libncurses/DEBIAN/control"  \
    \
    && dpkg-deb -b "libncurses"
