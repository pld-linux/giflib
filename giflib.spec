Summary:	GIF-manipulation library
Summary(es):	Biblioteca de manipulaci�n de archivos GIF
Summary(pl):	Biblioteka do obr�bki plik�w GIF
Summary(pt_BR):	Biblioteca de manipula��o de arquivos GIF
Summary(ru):	���������� ��� ������ � GIF-�������
Summary(uk):	��̦����� ��� ������ � GIF-�������
Name:		giflib
Version:	4.1.0
%define		so_ver	4.1.0
Release:	3
License:	X Consortium-like
Group:		Libraries
# not original URL, but working
Source0:	http://www.netsw.org/graphic/bitmap/formats/gif/giflib/%{name}-%{version}.tar.gz
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/libungif-man-pages.tar.bz2
Patch0:		%{name}-fixes-from-libungif.patch
URL:		http://prtr-13.ucsc.edu/~badger/software/libungif/giflib.shtml
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	netpbm-devel
BuildRequires:	urt-devel
Provides:	libungif.so.4
Provides:	libungif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libungif
Obsoletes:	libungif4

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
Summary:	GIF-manipulation library header files and documentation.
Summary(es):	Archivos de inclusi�n, bibliotecas para biblioteca de manipulaci�n de GIF
Summary(pl):	Pliki nag��wkowe oraz dokumentacja do formatu GIF
Summary(pt_BR):	Arquivos de inclus�o, bibliotecas para biblioteca de manipula��o de GIF
Summary(ru):	������, ���������� � ������������ GIF-����������
Summary(uk):	������, ¦�̦����� �� ���������æ� GIF-¦�̦�����
Group:		Development/Libraries
Requires:	%{name} = %{version}
Provides:	libungif-devel
Provides:	libungif.so
Obsoletes:	libungif-devel
Obsoletes:	libungif4-devel

%description devel
Libraries and headers needed for developing programs that use libgif
to load and save gif image files.

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
%{pkg_name} ��� �������� � ���������� ����������� � ������� GIF.

%description devel -l uk
������ �� ¦�̦�����, ����Ȧ�Φ ��� �������� �������, ��
�������������� %{pkg_name} ��� �������� �� ���������� ��������� �
�����Ԧ GIF.

%package static
Summary:	GIF-manipulation static library.
Summary(pl):	Biblioteki statyczne do obr�bki plik�w GIF
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com libungif
Summary(ru):	����������� ���������� GIF-����������
Summary(uk):	������Φ ¦�̦����� GIF-¦�̦�����
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Provides:	libungif-static
Obsoletes:	libungif-static

%description static
Static libraries needed for developing programs that use libgif to
load and save gif image files.

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
Summary:	Programs for converting and transforming gif images
Summary(pl):	Programy do konwertowania plik�w w formacie GIF
Summary(ru):	��������� ��� ��������������� � ��������� GIF-������
Summary(uk):	�������� ��� ������������� �� ������� GIF-���̦�
Group:		Applications/Graphics
Requires:	%{name} = %{version}
Provides:	libungif-progs
Obsoletes:	libungif-progs

%description progs
This package contains various programs for manipulating gif image
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
%patch -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
CFLAGS="%{rpmcflags} -fwritable-strings"; export CFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR="$RPM_BUILD_ROOT" install

ln -sf libgif.so.%{so_ver} $RPM_BUILD_ROOT%{_libdir}/libungif.so.%{so_ver}
ln -sf libgif.so.%{so_ver} $RPM_BUILD_ROOT%{_libdir}/libungif.so.4
ln -sf libgif.so.%{so_ver} $RPM_BUILD_ROOT%{_libdir}/libungif.so
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
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/libungif.so.4

%files devel
%defattr(644,root,root,755)
%doc doc/*.{txt,png} doc/{gif_lib,index,liberror}.html
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%doc doc/gif2* doc/gif[a-z]* doc/*2gif*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
