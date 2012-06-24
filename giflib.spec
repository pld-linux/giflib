Summary:	GIF-manipulation library
Summary(es):	Biblioteca de manipulaci�n de archivos GIF
Summary(pl):	Biblioteka do obr�bki plik�w GIF
Summary(pt_BR):	Biblioteca de manipula��o de arquivos GIF
Summary(ru):	���������� ��� ������ � GIF-�������
Summary(uk):	��̦����� ��� ������ � GIF-�������
Name:		giflib
Version:	4.1.4
Release:	4
License:	X Consortium-like
Group:		Libraries
Source0:	http://dl.sourceforge.net/libungif/%{name}-%{version}.tar.bz2
# Source0-md5:	827d338961482a986f39c7f114531636
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/libungif-man-pages.tar.bz2
# Source1-md5:	580c50403ed8f7e678ed04b3e0d712f3
Patch0:		%{name}-link.patch
Patch1:		http://users.own-hero.net/~decoder/fuzzyocr/giftext-segfault.patch
URL:		http://sourceforge.net/projects/libungif/
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	netpbm-devel
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	urt-devel
BuildRequires:	xorg-lib-libX11-devel
%ifarch %{x8664} ia64 ppc64 s390x sparc64
Provides:	libungif.so.4()(64bit)
%else
Provides:	libungif.so.4
%endif
Provides:	libungif
Obsoletes:	libungif
Obsoletes:	libungif4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GIF loading and saving shared library. This version uses LZW
compression (warning: patent/license issues in some countries).

%description -l es
Es una biblioteca compartida para carga y grabaci�n de archivos GIF.

%description -l pl
Biblioteki dynamiczne do kompresowania i dekompresowania plik�w w
formacie GIF. Ta wersja przy zapisie u�ywa konwersji LZW (uwaga: w
niekt�rych krajach powoduje to problemy zwi�zane z patentem i
konieczno�ci� nabycia licencji).

%description -l pt_BR
Biblioteca compartilhada para carga e grava��o de arquivos GIF.

%description -l ru
���������� ��� �������� � ���������� GIF-������.

%description -l uk
��̦����� ��� �������� �� ���������� GIF-���̦�.

%package devel
Summary:	GIF-manipulation library header files and documentation
Summary(es):	Archivos de inclusi�n, bibliotecas para biblioteca de manipulaci�n de GIF
Summary(pl):	Pliki nag��wkowe oraz dokumentacja do formatu GIF
Summary(pt_BR):	Arquivos de inclus�o, bibliotecas para biblioteca de manipula��o de GIF
Summary(ru):	������, ���������� � ������������ GIF-����������
Summary(uk):	������, ¦�̦����� �� ���������æ� GIF-¦�̦�����
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel
Provides:	libungif-devel
Obsoletes:	libungif-devel
Obsoletes:	libungif4-devel

%description devel
Libraries and headers needed for developing programs that use libgif
to load and save GIF image files.

%description devel -l es
Archivos de inclusi�n, bibliotecas y documentaci�n para biblioteca de
manipulaci�n de GIF.

%description devel -l pl
Biblioteki i pliki nag��wkowe niezb�dne przy kompilacji program�w
wykorzystuj�cych libgif.

%description devel -l pt_BR
Arquivos de inclus�o, bibliotecas para biblioteca de manipula��o de
GIF.

%description devel -l ru
������ � ����������, ����������� ��� ���������� ��������, ������������
giflib ��� �������� � ���������� ����������� � ������� GIF.

%description devel -l uk
������ �� ¦�̦�����, ����Ȧ�Φ ��� �������� �������, ��
�������������� giflib ��� �������� �� ���������� ��������� � �����Ԧ
GIF.

%package static
Summary:	GIF-manipulation static library
Summary(pl):	Biblioteki statyczne do obr�bki plik�w GIF
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com libungif
Summary(ru):	����������� ���������� GIF-����������
Summary(uk):	������Φ ¦�̦����� GIF-¦�̦�����
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	libungif-static
Obsoletes:	libungif-static

%description static
Static libraries needed for developing programs that use libgif to
load and save GIF image files.

%description static -l pl
Biblioteki statyczne do obr�bki plik�w GIF.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com libgif.

%description static -l ru
��� ��������� ����� �� ������������ ������������, ������� ������ ��
������ � libgif-devel.

%description static -l uk
�� ������� ����� ڦ ���������� ¦�̦�������, �� ¦���� �� ������� ��
������ libgif-devel.

%package progs
Summary:	Programs for converting and transforming GIF images
Summary(pl):	Programy do konwertowania plik�w w formacie GIF
Summary(ru):	��������� ��� ��������������� � ��������� GIF-������
Summary(uk):	�������� ��� ������������� �� ������� GIF-���̦�
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Provides:	libungif-progs
Obsoletes:	libungif-progs

%description progs
This package contains various programs for manipulating GIF image
files.

%description progs -l pl
Ten pakiet zawiera r�norodne programy obs�uguj�ce pliki w formacie
GIF.

%description progs -l ru
���� ����� �������� ��������� ��������� ��� ��������� GIF-������.

%description progs -l uk
��� ����� ͦ����� Ҧ�����Φ�Φ �������� ��� ������� GIF-���̦�.

%prep
%setup -q
%patch0 -p1
cd util
%patch1 -p0

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd $RPM_BUILD_ROOT%{_libdir}
ln -sf libgif.so.*.*.* $RPM_BUILD_ROOT%{_libdir}/libungif.so.4
ln -sf libgif.so.*.*.* $RPM_BUILD_ROOT%{_libdir}/libungif.so
ln -sf libgif.a $RPM_BUILD_ROOT%{_libdir}/libungif.a
ln -sf libgif.la $RPM_BUILD_ROOT%{_libdir}/libungif.la

install -d $RPM_BUILD_ROOT%{_mandir}
bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS COPYING ChangeLog NEWS PATENT_PROBLEMS README TODO
%attr(755,root,root) %{_libdir}/libgif.so.*.*.*
%attr(755,root,root) %{_libdir}/libungif.so.4

%files devel
%defattr(644,root,root,755)
%doc doc/*.{txt,png} doc/{gif_lib,index,liberror}.html
%attr(755,root,root) %{_libdir}/libgif.so
%attr(755,root,root) %{_libdir}/libungif.so
%{_libdir}/libgif.la
%{_libdir}/libungif.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libgif.a
%{_libdir}/libungif.a

%files progs
%defattr(644,root,root,755)
%doc doc/gif2* doc/gif[a-z]* doc/*2gif*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
