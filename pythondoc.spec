Summary:	Extracts information from Python objects, and generates reference manuals and indices
Summary(pl):	Narz�dzie tworz�ce manuale i indeksy z informacji wyci�gni�tych z obiekt�w Pythona
Name:		pythondoc
Version:	0.7
Release:	1
License:	Free
Group:		Development/Languages/Python
Source0:	http://starship.python.net/crew/danilo/pythondoc/%{name}_07.zip
# Source0-md5:	b4defb3a33ea44e68e374810a07adba8
Patch0:		%{name}-DESTDIR.patch
URL:		http://starship.python.net/crew/danilo/pythondoc/
BuildRequires:	python
Requires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define python_prefix  %(echo `python -c "import sys; print sys.prefix"`)
%define python_version %(echo `python -c "import sys; print sys.version[:3]"`)
%define python_libdir      %{python_prefix}/lib/python%{python_version}
%define python_includedir  %{python_prefix}/include/python%{python_version}
%define python_sitedir     %{python_libdir}/site-packages

%description
Pythondoc is a tool that extracts information from Python objects, and
generates reference manuals and indices. For best results use
StructuredText markup in your docstrings. A quick guide to
StructuredText may be found at
http://www.zope.org/Members/millejoh/structuredText.

%description -l pl
Pythondoc to narz�dzie wyci�gaj�ce informacje z obiekt�w Pythona i
generuj�ce na ich podstawie manuale i indeksy. Najlepiej u�ywa�
oznacze� StructuredText. Wprowadzenie do niego mo�na znale�� pod:
http://www.zope.org/Members/millejoh/structuredText.

%prep
%setup -q -n %{name}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -name '*.py' -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{name}/LICENSE.TXT* %{name}/README.html
%attr(755,root,root) %{_bindir}/*
%{python_sitedir}/%{name}
