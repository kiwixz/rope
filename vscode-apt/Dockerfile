FROM {{base_image}}

WORKDIR "/root"

ARG VERSION
COPY "control" "vscode-apt-$VERSION/DEBIAN/"
COPY "vscode.list" "vscode-apt-$VERSION/etc/apt/sources.list.d/"
COPY "microsoft.gpg" "vscode-apt-$VERSION/etc/apt/trusted.gpg.d/"

RUN sed -i "s/{{version}}/$VERSION/g" "vscode-apt-$VERSION/DEBIAN/control"  \
    && dpkg-deb -b "vscode-apt-$VERSION"
