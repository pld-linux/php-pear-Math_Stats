%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	Stats
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_class}_%{_subclass} - Classes to calculate statistical parameters
Summary(pl):	%{_class}_%{_subclass} - klasy do obliczania parametrów statystycznych
Name:		php-pear-%{_pearname}
Version:	0.9.0
%define	_beta beta3
%define	_rel 2
Release:	0.%{_beta}.%{_rel}
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_beta}.tgz
# Source0-md5:	ffc0b653e5e2985113262a5299ebe69b
URL:		http://pear.php.net/package/Math_Stats/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Classes to calculate statistical parameters of numerical arrays of
data. The data can be in a simple numerical array, or in a cummulative
numerical array. A cummulative array, has the value as the index and
the number of repeats as the value for the array item, e.g. $data =
array(3=>4, 2.3=>5, 1.25=>6, 0.5=>3). Nulls can be rejected, ignored
or handled as zero values.

In PEAR status of this package is: %{_status}.

%description -l pl
Ten pakiet zawiera klasy s³u¿±ce do obliczania parametrów
statystycznych z tablic danych. Dane mog± byæ w zwyk³ej tablicy
numerycznej lub w tablicy skumulowanej. Tablica skumulowana zawiera
indeksy i liczby wyst±pieñ warto¶ci dla elementu tablicy, np. $data =
array(3=>4, 2.3=>5, 1.25=>6, 0.5=>3). Puste elementy mog± byæ
odrzucone, ignorowane lub taktowane jako warto¶ci zerowe.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

install -d docs/%{_pearname}/examples
mv ./%{php_pear_dir}/%{_class}/examples/* docs/%{_pearname}/examples

install -d ./%{php_pear_dir}/tests/%{_pearname}
mv ./%{php_pear_dir}/{%{_class}/test/*,tests/%{_pearname}}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
