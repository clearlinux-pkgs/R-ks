#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ks
Version  : 1.11.4
Release  : 11
URL      : https://cran.r-project.org/src/contrib/ks_1.11.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ks_1.11.4.tar.gz
Summary  : Kernel Smoothing
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-ks-lib = %{version}-%{release}
BuildRequires : R-FNN
BuildRequires : R-kernlab
BuildRequires : R-mclust
BuildRequires : R-multicool
BuildRequires : R-mvtnorm
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-ks package.
Group: Libraries

%description lib
lib components for the R-ks package.


%prep
%setup -q -c -n ks

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552890512

%install
export SOURCE_DATE_EPOCH=1552890512
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ks
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ks
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ks
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  ks || :


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
/usr/lib64/R/library/ks/data/quake.RData
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
/usr/lib64/R/library/ks/libs/ks.so
/usr/lib64/R/library/ks/libs/ks.so.avx2
/usr/lib64/R/library/ks/libs/ks.so.avx512
