Summary:	Pythondoc - tool that extracts information from Python objects, and generates reference manuals and indices
Name:		pythondoc
Version:	0.7
Release:	1
License:	free
Group:		Languages/Python
Source0:	http://starship.python.net/crew/danilo/pythondoc/pythondoc_07.zip
Patch0:		%{name}-DESTDIR.patch
URL:		http://starship.python.net/crew/danilo/pythondoc/
BuildPrereq:	python
Requires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define python_prefix  %(echo `python -c "import sys; print sys.prefix"`)
%define python_version %(echo `python -c "import sys; print sys.version[:3]"`)
%define python_libdir      %{python_prefix}/lib/python%{python_version}
%define python_includedir  %{python_prefix}/include/python%{python_version}
%define python_sitedir     %{python_libdir}/site-packages

%description
Pythondoc is a tool that extracts information from Python objects,
and generates reference manuals and indices. For best results use
StructuredText markup in your docstrings. 
A quick guide to StructuredText may be found at
http://www.zope.org/Members/millejoh/structuredText.

%prep
%setup  -q -c -T
unzip -qa %{SOURCE0}
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
cd %{name}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -name '*.py' -exec rm {} \;

gzip -9nf LICENSE.TXT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{name}/LICENSE.TXT* %{name}/README.html 
%attr(755,root,root) %{_bindir}/*
%{python_sitedir}/%{name}
