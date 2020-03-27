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
COPY "clang_tools.control" "/root/clang-tools-$MAJOR-$VERSION/DEBIAN/control"
COPY "meta_clang_tools.control" "/root/clang-tools-$VERSION/DEBIAN/control"
COPY "clangd.control" "/root/clangd-$MAJOR-$VERSION/DEBIAN/control"
COPY "meta_clangd.control" "/root/clangd-$VERSION/DEBIAN/control"
COPY "lld.control" "/root/lld-$VERSION/DEBIAN/control"
COPY "lldb.control" "/root/lldb-$VERSION/DEBIAN/control"

RUN sed -i "s/{{version}}/$VERSION/g; s/{{major}}/$MAJOR/g"  \
        "/root/clang-$VERSION/DEBIAN/control"  \
        "/root/clang-$MAJOR-$VERSION/DEBIAN/control"  \
        "/root/clang-tools-$VERSION/DEBIAN/control"  \
        "/root/clang-tools-$MAJOR-$VERSION/DEBIAN/control"  \
        "/root/clangd-$VERSION/DEBIAN/control"  \
        "/root/clangd-$MAJOR-$VERSION/DEBIAN/control"  \
        "/root/lld-$VERSION/DEBIAN/control"  \
        "/root/lldb-$VERSION/DEBIAN/control"  \
    \
    && mkdir -p "/root/clang-$VERSION/usr/bin/"  \
    && ln -s "clang-$MAJOR" "/root/clang-$VERSION/usr/bin/clang"  \
    && ln -s "clang++-$MAJOR" "/root/clang-$VERSION/usr/bin/clang++"  \
    && dpkg-deb -b "/root/clang-$VERSION"  \
    && mkdir -p "/root/clang-$MAJOR-$VERSION/usr/bin/"  \
    && cp "bin/clang-$MAJOR" "/root/clang-$MAJOR-$VERSION/usr/bin/"  \
    && ln -s "clang-$MAJOR" "/root/clang-$MAJOR-$VERSION/usr/bin/clang++-$MAJOR"  \
    && mkdir -p "/root/clang-$MAJOR-$VERSION/usr/lib/"  \
    && cp -R "lib/clang/" "/root/clang-$MAJOR-$VERSION/usr/lib/"  \
    && dpkg-deb -b "/root/clang-$MAJOR-$VERSION"  \
    \
    && mkdir -p "/root/clang-tools-$VERSION/usr/bin/"  \
    && ln -s "clang-format-$MAJOR" "/root/clang-tools-$VERSION/usr/bin/clang-format"  \
    && ln -s "clang-tidy-$MAJOR" "/root/clang-tools-$VERSION/usr/bin/clang-tidy"  \
    && dpkg-deb -b "/root/clang-tools-$VERSION"  \
    && mkdir -p "/root/clang-tools-$MAJOR-$VERSION/usr/bin/"  \
    && cp "bin/clang-format" "/root/clang-tools-$MAJOR-$VERSION/usr/bin/clang-format-$MAJOR"  \
    && cp "bin/clang-tidy" "/root/clang-tools-$MAJOR-$VERSION/usr/bin/clang-tidy-$MAJOR"  \
    && dpkg-deb -b "/root/clang-tools-$MAJOR-$VERSION"  \
    \
    && mkdir -p "/root/clangd-$VERSION/usr/bin/"  \
    && ln -s "clangd-$MAJOR" "/root/clangd-$VERSION/usr/bin/clangd"  \
    && dpkg-deb -b "/root/clangd-$VERSION"  \
    && mkdir -p "/root/clangd-$MAJOR-$VERSION/usr/bin/"  \
    && cp "bin/clangd" "/root/clangd-$MAJOR-$VERSION/usr/bin/clangd-$MAJOR"  \
    && dpkg-deb -b "/root/clangd-$MAJOR-$VERSION"  \
    \
    && mkdir -p "/root/lld-$VERSION/usr/bin/"  \
    && cp "bin/lld" "/root/lld-$VERSION/usr/bin/"  \
    && dpkg-deb -b "/root/lld-$VERSION"  \
    \
    && mkdir -p "/root/lldb-$VERSION/usr/bin/"  \
    && cp "bin/lldb" "/root/lldb-$VERSION/usr/bin/"  \
    && dpkg-deb -b "/root/lldb-$VERSION"
