#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : R-lbfgsb3c
Version  : 2024.3.5
Release  : 10
URL      : https://cran.r-project.org/src/contrib/lbfgsb3c_2024-3.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/lbfgsb3c_2024-3.5.tar.gz
Summary  : Limited Memory BFGS Minimizer with Bounds on Parameters with
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: R-lbfgsb3c-lib = %{version}-%{release}
Requires: R-lbfgsb3c-license = %{version}-%{release}
Requires: R-Rcpp
Requires: R-RcppArmadillo
Requires: R-numDeriv
BuildRequires : R-Rcpp
BuildRequires : R-RcppArmadillo
BuildRequires : R-RcppArmadillo-dev
BuildRequires : R-numDeriv
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<!-- badges: start -->
[![R-CMD-check](https://github.com/nlmixr2/lbfgsb3c/actions/workflows/R-CMD-check.yaml/badge.svg)](https://github.com/nlmixr2/lbfgsb3c/actions/workflows/R-CMD-check.yaml)
[![CRAN total downloads](https://cranlogs.r-pkg.org/badges/grand-total/lbfgsb3c)](https://cran.r-project.org/package=lbfgsb3c)
[![CRAN total downloads](https://cranlogs.r-pkg.org/badges/lbfgsb3c)](https://cran.r-project.org/package=lbfgsb3c)
[![Codecov test coverage](https://codecov.io/gh/nlmixr2/lbfgsb3c/branch/main/graph/badge.svg)](https://app.codecov.io/gh/nlmixr2/lbfgsb3c?branch=main)
<!-- badges: end -->

%package lib
Summary: lib components for the R-lbfgsb3c package.
Group: Libraries
Requires: R-lbfgsb3c-license = %{version}-%{release}

%description lib
lib components for the R-lbfgsb3c package.


%package license
Summary: license components for the R-lbfgsb3c package.
Group: Default

%description license
license components for the R-lbfgsb3c package.


%prep
%setup -q -n lbfgsb3c
pushd ..
cp -a lbfgsb3c buildavx2
popd
pushd ..
cp -a lbfgsb3c buildavx512
popd
pushd ..
cp -a lbfgsb3c buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1740094815

%install
export SOURCE_DATE_EPOCH=1740094815
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-lbfgsb3c
cp %{_builddir}/lbfgsb3c/inst/License-lbfgsb-orig.txt %{buildroot}/usr/share/package-licenses/R-lbfgsb3c/7521b5b33f064a3d0649bdbd4a7c0c026a6fe398 || :
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
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
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
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/lbfgsb3c/DESCRIPTION
/usr/lib64/R/library/lbfgsb3c/INDEX
/usr/lib64/R/library/lbfgsb3c/License-lbfgsb-orig.txt
/usr/lib64/R/library/lbfgsb3c/Meta/Rd.rds
/usr/lib64/R/library/lbfgsb3c/Meta/features.rds
/usr/lib64/R/library/lbfgsb3c/Meta/hsearch.rds
/usr/lib64/R/library/lbfgsb3c/Meta/links.rds
/usr/lib64/R/library/lbfgsb3c/Meta/nsInfo.rds
/usr/lib64/R/library/lbfgsb3c/Meta/package.rds
/usr/lib64/R/library/lbfgsb3c/Meta/vignette.rds
/usr/lib64/R/library/lbfgsb3c/NAMESPACE
/usr/lib64/R/library/lbfgsb3c/NEWS.md
/usr/lib64/R/library/lbfgsb3c/R/lbfgsb3c
/usr/lib64/R/library/lbfgsb3c/R/lbfgsb3c.rdb
/usr/lib64/R/library/lbfgsb3c/R/lbfgsb3c.rdx
/usr/lib64/R/library/lbfgsb3c/doc/index.html
/usr/lib64/R/library/lbfgsb3c/doc/lbfgsb3c.R
/usr/lib64/R/library/lbfgsb3c/doc/lbfgsb3c.Rmd
/usr/lib64/R/library/lbfgsb3c/doc/lbfgsb3c.html
/usr/lib64/R/library/lbfgsb3c/drlbfgsb3.R
/usr/lib64/R/library/lbfgsb3c/help/AnIndex
/usr/lib64/R/library/lbfgsb3c/help/aliases.rds
/usr/lib64/R/library/lbfgsb3c/help/lbfgsb3c.rdb
/usr/lib64/R/library/lbfgsb3c/help/lbfgsb3c.rdx
/usr/lib64/R/library/lbfgsb3c/help/paths.rds
/usr/lib64/R/library/lbfgsb3c/html/00Index.html
/usr/lib64/R/library/lbfgsb3c/html/R.css
/usr/lib64/R/library/lbfgsb3c/include/lbfgsb3c.h
/usr/lib64/R/library/lbfgsb3c/include/lbfgsb3ptr.h
/usr/lib64/R/library/lbfgsb3c/include/lbfgsb3x.h
/usr/lib64/R/library/lbfgsb3c/lbfgsb140731.f
/usr/lib64/R/library/lbfgsb3c/tests/testthat.R
/usr/lib64/R/library/lbfgsb3c/tests/testthat/test-240319.R
/usr/lib64/R/library/lbfgsb3c/tests/testthat/test-bounds.R
/usr/lib64/R/library/lbfgsb3c/tests/testthat/test-cyq.R
/usr/lib64/R/library/lbfgsb3c/tests/testthat/test-genrose.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/lbfgsb3c/libs/lbfgsb3c.so
/V4/usr/lib64/R/library/lbfgsb3c/libs/lbfgsb3c.so
/VA/usr/lib64/R/library/lbfgsb3c/libs/lbfgsb3c.so
/usr/lib64/R/library/lbfgsb3c/libs/lbfgsb3c.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-lbfgsb3c/7521b5b33f064a3d0649bdbd4a7c0c026a6fe398
