%include	/usr/lib/rpm/macros.php
%define		_status		beta
%define		_pearname	Math_Stats
Summary:	Math_Stats - Classes to calculate statistical parameters
Summary(pl.UTF-8):	Math_Stats - klasy do obliczania parametrów statystycznych
Name:		php-pear-%{_pearname}
Version:	0.9.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	afb06c6975bd1a53c97a8db4fd5d3546
URL:		http://pear.php.net/package/Math_Stats/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
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

%description -l pl.UTF-8
Ten pakiet zawiera klasy służące do obliczania parametrów
statystycznych z tablic danych. Dane mogą być w zwykłej tablicy
numerycznej lub w tablicy skumulowanej. Tablica skumulowana zawiera
indeksy i liczby wystąpień wartości dla elementu tablicy, np. $data =
array(3=>4, 2.3=>5, 1.25=>6, 0.5=>3). Puste elementy mogą być
odrzucone, ignorowane lub taktowane jako wartości zerowe.

Ta klasa ma w PEAR status: %{_status}.


%prep
%pear_package_setup

mv docs/%{_pearname}/docs/examples .

mv .%{php_pear_dir}/contrib .
mv .%{php_pear_dir}/data/Math_Stats/contrib/ignatius_reilly/* contrib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/* contrib
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Math/Stats.php

%{_examplesdir}/%{name}-%{version}
