FROM {{base_image}}

RUN apt update  \
    && apt -y full-upgrade  \
    && apt -y install  \
        git openssh-client  \
        cmake clang g++ lld ninja-build

ARG REF=master
RUN git clone --branch=$REF "https://github.com/llvm/llvm-project" "/root/llvm"  \
    && mkdir "/root/llvm/build"
WORKDIR "/root/llvm/build"

RUN CC="clang" CXX="clang++" cmake -G "Ninja"  \
        -D "CMAKE_BUILD_TYPE=Release"  \
        -D "LLVM_ENABLE_PROJECTS=clang;clang-tools-extra;compiler-rt;lld;lldb"  \
        -D "LLVM_ENABLE_LLD=ON"  \
        -D "LLVM_ENABLE_LTO=Thin"  \
        "../llvm"  \
    && ninja

ARG VERSION=$REF
ARG MAJOR=git
COPY "clang.control" "/root/clang-$MAJOR-$VERSION/DEBIAN/control"
COPY "meta_clang.control" "/root/clang-$VERSION/DEBIAN/control"

RUN sed -i "s/{{version}}/$VERSION/g; s/{{major}}/$MAJOR/g"  \
        "/root/clang-$VERSION/DEBIAN/control" "/root/clang-$MAJOR-$VERSION/DEBIAN/control"  \
    && mkdir -p "/root/clang-$VERSION/usr/bin/"  \
    && ln -s "clang-$MAJOR" "/root/clang-$VERSION/usr/bin/clang"  \
    && ln -s "clang++-$MAJOR" "/root/clang-$VERSION/usr/bin/clang++"  \
    && dpkg-deb -b "/root/clang-$VERSION"  \
    && mkdir -p "/root/clang-$MAJOR-$VERSION/usr/bin/"  \
    && cp "bin/clang-$MAJOR" "/root/clang-$MAJOR-$VERSION/usr/bin/"  \
    && ln -s "clang-$MAJOR" "/root/clang-$MAJOR-$VERSION/usr/bin/clang++-$MAJOR"  \
    && dpkg-deb -b "/root/clang-$MAJOR-$VERSION"
