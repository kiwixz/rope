FROM {{base_image}}

RUN apt update  \
    && apt -y full-upgrade  \
    && apt -y install  \
        git openssh-client  \
        cargo make  \
        cmake g++ pkg-config python3  \
        {{apt_libs}}

ARG REF=master
RUN git clone --branch=$REF "https://github.com/alacritty/alacritty" "/root/alacritty"
WORKDIR "/root/alacritty"

RUN make binary

ARG VERSION=$REF
COPY "control" "/root/alacritty-$VERSION/DEBIAN/"

RUN sed -i "s/{{version}}/$VERSION/g" "/root/alacritty-$VERSION/DEBIAN/control"  \
    && cp "extra/linux/debian/postinst" "extra/linux/debian/prerm" "/root/alacritty-$VERSION/DEBIAN/"  \
    && chmod +x "/root/alacritty-$VERSION/DEBIAN/postinst" "/root/alacritty-$VERSION/DEBIAN/prerm"  \
    && mkdir -p  \
        "/root/alacritty-$VERSION/usr/bin/"  \
        "/root/alacritty-$VERSION/usr/share/applications/"  \
        "/root/alacritty-$VERSION/usr/share/pixmaps/"  \
        "/root/alacritty-$VERSION/usr/share/bash-completion/completions/"  \
        "/root/alacritty-$VERSION/usr/share/fish/completions/"  \
        "/root/alacritty-$VERSION/usr/share/zsh/vendor-completions/"  \
    && cp "target/release/alacritty" "/root/alacritty-$VERSION/usr/bin/"  \
    && cp "extra/linux/alacritty.desktop" "/root/alacritty-$VERSION/usr/share/applications/"  \
    && cp "extra/logo/alacritty-term.svg" "/root/alacritty-$VERSION/usr/share/pixmaps/Alacritty.svg"  \
    && cp "extra/completions/alacritty.bash" "/root/alacritty-$VERSION/usr/share/bash-completion/completions/"  \
    && cp "extra/completions/alacritty.fish" "/root/alacritty-$VERSION/usr/share/fish/completions/"  \
    && cp "extra/completions/_alacritty" "/root/alacritty-$VERSION/usr/share/zsh/vendor-completions/"  \
    && dpkg-deb -b "/root/alacritty-$VERSION"