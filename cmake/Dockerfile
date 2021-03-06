FROM {{base_image}}

RUN apt update  \
    && apt -y --no-install-recommends upgrade  \
        git ca-certificates  \
        clang-10 lld-10 make  \
        libncurses-dev libssl-dev

ARG REF=master
RUN git clone --branch=$REF "https://gitlab.kitware.com/cmake/cmake" "/root/cmake"
WORKDIR "/root/cmake/build"

RUN PARALLEL=$(($(nproc) + 2))  \
    && CC=clang-10 CXX=clang++-10  \
        CXXFLAGS="-flto=thin -fuse-ld=lld -Wno-unused-command-line-argument"  \
        CFLAGS="$CXXFLAGS"  \
        ../bootstrap --parallel=$PARALLEL \
    && make -j $PARALLEL

ARG VERSION=$REF
COPY "control" "/root/cmake-$VERSION/DEBIAN/"

SHELL ["/bin/bash", "-c"]
RUN MAJOR_MINOR="${VERSION%.*}"  \
    && sed -i "s/{{version}}/$VERSION/g" "/root/cmake-$VERSION/DEBIAN/control"  \
    && mkdir -p /root/cmake-$VERSION/usr/{bin,share/{cmake-$MAJOR_MINOR,bash-completion/completions}}/  \
    && cp bin/c{{,c}make,pack,test} "/root/cmake-$VERSION/usr/bin/"  \
    && cp -r ../{Modules,Templates} "/root/cmake-$VERSION/usr/share/cmake-$MAJOR_MINOR/"  \
    && cp ../Auxiliary/bash-completion/c{make,pack,test} "/root/cmake-$VERSION/usr/share/bash-completion/completions/"  \
    && strip /root/cmake-$VERSION/usr/bin/*  \
    && dpkg-deb -b "/root/cmake-$VERSION"
