FROM {{base_image}}

WORKDIR "/root"

COPY "ncurses.control" "libncurses/DEBIAN/control"
COPY "libpython.control" "libpython3/DEBIAN/control"

RUN sed -i "s/{{version}}/{{ncurses_version}}/g"  \
        "libncurses/DEBIAN/control"  \
    && dpkg-deb -b "libncurses"  \
    \
    && sed -i "s/{{version}}/{{py_version}}/g"  \
        "libpython3/DEBIAN/control"  \
    && dpkg-deb -b "libpython3"
