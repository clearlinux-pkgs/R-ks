#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v20
# autospec commit: f35655a
#
Name     : R-ks
Version  : 1.14.3
Release  : 62
URL      : https://cran.r-project.org/src/contrib/ks_1.14.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ks_1.14.3.tar.gz
Summary  : Kernel Smoothing
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-ks-lib = %{version}-%{release}
Requires: R-FNN
Requires: R-kernlab
Requires: R-mclust
Requires: R-multicool
Requires: R-mvtnorm
Requires: R-pracma
BuildRequires : R-FNN
BuildRequires : R-kernlab
BuildRequires : R-mclust
BuildRequires : R-multicool
BuildRequires : R-mvtnorm
BuildRequires : R-pracma
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package lib
Summary: lib components for the R-ks package.
Group: Libraries

%description lib
lib components for the R-ks package.


%prep
%setup -q -n ks
pushd ..
cp -a ks buildavx2
popd
pushd ..
cp -a ks buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1727045036

%install
export SOURCE_DATE_EPOCH=1727045036
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ks/DESCRIPTION
/usr/lib64/R/library/ks/INDEX
/usr/lib64/R/library/ks/Meta/Rd.rds
/usr/lib64/R/library/ks/Meta/data.rds
/usr/lib64/R/library/ks/Meta/features.rds
/usr/lib64/R/library/ks/Meta/hsearch.rds
/usr/lib64/R/library/ks/Meta/links.rds
/usr/lib64/R/library/ks/Meta/nsInfo.rds
/usr/lib64/R/library/ks/Meta/package.rds
/usr/lib64/R/library/ks/Meta/vignette.rds
/usr/lib64/R/library/ks/NAMESPACE
/usr/lib64/R/library/ks/R/ks
/usr/lib64/R/library/ks/R/ks.rdb
/usr/lib64/R/library/ks/R/ks.rdx
/usr/lib64/R/library/ks/data/air.RData
/usr/lib64/R/library/ks/data/cardio.RData
/usr/lib64/R/library/ks/data/grevillea.RData
/usr/lib64/R/library/ks/data/hsct.RData
/usr/lib64/R/library/ks/data/plate.RData
/usr/lib64/R/library/ks/data/platesf.RData
/usr/lib64/R/library/ks/data/quake.RData
/usr/lib64/R/library/ks/data/quakesf.RData
/usr/lib64/R/library/ks/data/tempb.RData
/usr/lib64/R/library/ks/data/unicef.RData
/usr/lib64/R/library/ks/data/worldbank.RData
/usr/lib64/R/library/ks/doc/index.html
/usr/lib64/R/library/ks/doc/kde.R
/usr/lib64/R/library/ks/doc/kde.Rnw
/usr/lib64/R/library/ks/doc/kde.pdf
/usr/lib64/R/library/ks/help/AnIndex
/usr/lib64/R/library/ks/help/aliases.rds
/usr/lib64/R/library/ks/help/ks.rdb
/usr/lib64/R/library/ks/help/ks.rdx
/usr/lib64/R/library/ks/help/paths.rds
/usr/lib64/R/library/ks/html/00Index.html
/usr/lib64/R/library/ks/html/R.css

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/ks/libs/ks.so
/V4/usr/lib64/R/library/ks/libs/ks.so
/usr/lib64/R/library/ks/libs/ks.so
