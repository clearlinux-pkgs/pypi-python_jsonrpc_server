#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-python_jsonrpc_server
Version  : 0.4.0
Release  : 22
URL      : https://files.pythonhosted.org/packages/81/7d/c4c4102b94ef2e090d94fc02625653d3d3a0306e53ef24bcb6e9496bfc1e/python-jsonrpc-server-0.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/81/7d/c4c4102b94ef2e090d94fc02625653d3d3a0306e53ef24bcb6e9496bfc1e/python-jsonrpc-server-0.4.0.tar.gz
Summary  : JSON RPC 2.0 server library
Group    : Development/Tools
License  : MIT
Requires: pypi-python_jsonrpc_server-license = %{version}-%{release}
Requires: pypi-python_jsonrpc_server-python = %{version}-%{release}
Requires: pypi-python_jsonrpc_server-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(future)
BuildRequires : pypi(ujson)

%description
======================

%package license
Summary: license components for the pypi-python_jsonrpc_server package.
Group: Default

%description license
license components for the pypi-python_jsonrpc_server package.


%package python
Summary: python components for the pypi-python_jsonrpc_server package.
Group: Default
Requires: pypi-python_jsonrpc_server-python3 = %{version}-%{release}

%description python
python components for the pypi-python_jsonrpc_server package.


%package python3
Summary: python3 components for the pypi-python_jsonrpc_server package.
Group: Default
Requires: python3-core
Provides: pypi(python_jsonrpc_server)
Requires: pypi(ujson)

%description python3
python3 components for the pypi-python_jsonrpc_server package.


%prep
%setup -q -n python-jsonrpc-server-0.4.0
cd %{_builddir}/python-jsonrpc-server-0.4.0
pushd ..
cp -a python-jsonrpc-server-0.4.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656401934
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-python_jsonrpc_server
cp %{_builddir}/python-jsonrpc-server-0.4.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-python_jsonrpc_server/4df3c87108ebab83aa7bb222e245d841c6574d4f
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-python_jsonrpc_server/4df3c87108ebab83aa7bb222e245d841c6574d4f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
