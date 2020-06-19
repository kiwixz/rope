FROM {{base_image}}

RUN apt update  \
    && apt -y --no-install-recommends upgrade  \
        git ca-certificates  \
        clang-10 lld-10 make  \
        libssl-dev

ARG REF=master
RUN git clone --branch=$REF "https://gitlab.kitware.com/cmake/cmake" "/root/cmake"
WORKDIR "/root/cmake"

RUN CC=clang-10 CXX=clang++-10  \
        CXXFLAGS="-flto=thin -fuse-ld=lld -Wno-unused-command-line-argument"  \
        CFLAGS="$CXXFLAGS"  \
        ./bootstrap  \
    && make -j $(($(nproc) + 2))

ARG VERSION=$REF
COPY "control" "/root/cmake-$VERSION/DEBIAN/"

RUN sed -i "s/{{version}}/$VERSION/g" "/root/cmake-$VERSION/DEBIAN/control"  \
    && mkdir -p "/root/cmake-$VERSION/usr/bin/"  \
    && cp "bin/c{{,c}make,pack,test}" "/root/cmake-$VERSION/usr/bin/"  \
    && dpkg-deb -b "/root/cmake-$VERSION"
