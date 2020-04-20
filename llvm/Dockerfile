FROM {{base_image}}

RUN apt update  \
    && apt -y full-upgrade  \
    && apt -y --no-install-recommends install  \
        git ca-certificates  \
        cmake clang-{{local_llvm}} g++ lld-{{local_llvm}} ninja-build  \
        libedit-dev liblzma-dev libncurses-dev libpfm4-dev  \
            libpython3-dev libxml2-dev libz3-dev python3 swig zlib1g-dev  \
        python3-distutils python3-pygments python3-yaml

ARG REF=master
RUN git clone --branch=$REF "https://github.com/llvm/llvm-project" "/root/llvm"  \
    && mkdir "/root/llvm/build"
WORKDIR "/root/llvm/build"

RUN CC="clang-{{local_llvm}}" CXX="clang++-{{local_llvm}}" cmake -G "Ninja"  \
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
    && ln -s "lld" "/root/lld-$VERSION/usr/bin/ld.lld"  \
    && dpkg-deb -b "/root/lld-$VERSION"  \
    \
    && mkdir -p "/root/lldb-$VERSION/usr/bin/"  \
    && cp "bin/lldb" "bin/lldb-server" "bin/lldb-vscode" "/root/lldb-$VERSION/usr/bin/"  \
    && mkdir -p "/root/lldb-$VERSION/usr/lib/"  \
    && cp "lib/liblldb.so.$VERSION" "/root/lldb-$VERSION/usr/lib/"  \
    && ln -s "liblldb.so.$VERSION" "/root/lldb-$VERSION/usr/lib/liblldb.so.$MAJOR"  \
    && ln -s "liblldb.so.$MAJOR" "/root/lldb-$VERSION/usr/lib/liblldb.so"  \
    && dpkg-deb -b "/root/lldb-$VERSION"
