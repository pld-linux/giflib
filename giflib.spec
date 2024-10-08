#
# Conditional build:
%bcond_without	tests	# regression tests

Summary:	GIF-manipulation library
Summary(es.UTF-8):	Biblioteca de manipulación de archivos GIF
Summary(pl.UTF-8):	Biblioteka do obróbki plików GIF
Summary(pt_BR.UTF-8):	Biblioteca de manipulação de arquivos GIF
Summary(ru.UTF-8):	Библиотека для работы с GIF-файлами
Summary(uk.UTF-8):	Бібліотека для роботи з GIF-файлами
Name:		giflib
Version:	5.2.2
Release:	2
License:	MIT-like
Group:		Libraries
Source0:	https://downloads.sourceforge.net/giflib/%{name}-%{version}.tar.gz
# Source0-md5:	913dd251492134e235ee3c9a91987a4d
Patch0:		%{name}-make.patch
Patch1:		%{name}-extern.patch
URL:		https://sourceforge.net/projects/giflib/
BuildRequires:	ImageMagick
BuildRequires:	gcc >= 5:3.2
BuildRequires:	netpbm-devel
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	sed
BuildRequires:	xmlto
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GIF loading and saving shared library. This version uses LZW
compression (warning: patent/license issues in some countries).

%description -l es.UTF-8
Es una biblioteca compartida para carga y grabación de archivos GIF.

%description -l pl.UTF-8
Biblioteki dynamiczne do kompresowania i dekompresowania plików w
formacie GIF. Ta wersja przy zapisie używa konwersji LZW (uwaga: w
niektórych krajach powoduje to problemy związane z patentem i
koniecznością nabycia licencji).

%description -l pt_BR.UTF-8
Biblioteca compartilhada para carga e gravação de arquivos GIF.

%description -l ru.UTF-8
Библиотека для загрузки и сохранения GIF-файлов.

%description -l uk.UTF-8
Бібліотека для загрузки та збереження GIF-файлів.

%package devel
Summary:	GIF-manipulation library header files and documentation
Summary(es.UTF-8):	Archivos de inclusión, bibliotecas para biblioteca de manipulación de GIF
Summary(pl.UTF-8):	Pliki nagłówkowe oraz dokumentacja do formatu GIF
Summary(pt_BR.UTF-8):	Arquivos de inclusão, bibliotecas para biblioteca de manipulação de GIF
Summary(ru.UTF-8):	Хедеры, библиотеки и документация GIF-библиотеки
Summary(uk.UTF-8):	Хедери, бібліотеки та документація GIF-бібліотеки
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	libungif-devel
Obsoletes:	giflib4-devel < 5
Obsoletes:	libungif-devel < 5

%description devel
Libraries and headers needed for developing programs that use libgif
to load and save GIF image files.

%description devel -l es.UTF-8
Archivos de inclusión, bibliotecas y documentación para biblioteca de
manipulación de GIF.

%description devel -l pl.UTF-8
Biblioteki i pliki nagłówkowe niezbędne przy kompilacji programów
wykorzystujących libgif.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão, bibliotecas para biblioteca de manipulação de
GIF.

%description devel -l ru.UTF-8
Хедеры и библиотеки, необходимые для разработки программ, использующих
giflib для загрузки и сохранения изображений в формате GIF.

%description devel -l uk.UTF-8
Хедери та бібліотеки, необхідні для розробки програм, що
використовують giflib для загрузки та збереження зображень у форматі
GIF.

%package static
Summary:	GIF-manipulation static library
Summary(pl.UTF-8):	Biblioteki statyczne do obróbki plików GIF
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com libungif
Summary(ru.UTF-8):	Статические библиотеки GIF-библиотеки
Summary(uk.UTF-8):	Статичні бібліотеки GIF-бібліотеки
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	libungif-static
Obsoletes:	giflib4-static < 5
Obsoletes:	libungif-static < 5

%description static
Static libraries needed for developing programs that use libgif to
load and save GIF image files.

%description static -l pl.UTF-8
Biblioteki statyczne do obróbki plików GIF.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com libgif.

%description static -l ru.UTF-8
Это отдельный пакет со статическими библиотеками, которые больше не
входят в libgif-devel.

%description static -l uk.UTF-8
Це окремий пакет зі статичними бібліотеками, що більше не входять до
складу libgif-devel.

%package progs
Summary:	Programs for converting and transforming GIF images
Summary(pl.UTF-8):	Programy do konwertowania plików w formacie GIF
Summary(ru.UTF-8):	Программы для конвертирования и обработки GIF-файлов
Summary(uk.UTF-8):	Програми для конвертування та обробки GIF-файлів
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Provides:	libungif-progs
Obsoletes:	giflib4-progs < 5
Obsoletes:	libungif-progs < 5

%description progs
This package contains various programs for manipulating GIF image
files.

%description progs -l pl.UTF-8
Ten pakiet zawiera różnorodne programy obsługujące pliki w formacie
GIF.

%description progs -l ru.UTF-8
Этот пакет содержит различные программы для обработки GIF-файлов.

%description progs -l uk.UTF-8
Цей пакет містить різноманітні програми для обробки GIF-файлів.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%if %{with tests}
ln -sf libgif.so libgif.so.7
ln -sf libgifutil.so libgifutil.so.7
LD_LIBRARY_PATH=$(pwd) \
%{__make} -j1 check
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir}

# wrong files installed in 5.2.2
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/*.xml
cp -p doc/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -d $RPM_BUILD_ROOT%{_mandir}/man7
cp -p doc/*.7 $RPM_BUILD_ROOT%{_mandir}/man7

# docs for not installed programs used in tests
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/{gifbg,gifcolor,gifecho,giffilter,gifhisto,gifinto,gifsponge,gifwedge}.1

cd $RPM_BUILD_ROOT%{_libdir}
ln -sf libgif.so.*.*.* $RPM_BUILD_ROOT%{_libdir}/libungif.so
ln -sf libgif.a $RPM_BUILD_ROOT%{_libdir}/libungif.a

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog NEWS README TODO history.adoc
%attr(755,root,root) %{_libdir}/libgif.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgif.so.7
%attr(755,root,root) %{_libdir}/libgifutil.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgifutil.so.7

%files devel
%defattr(644,root,root,755)
%doc doc/{gif_lib,intro}.html doc/whatsinagif
%attr(755,root,root) %{_libdir}/libgif.so
%attr(755,root,root) %{_libdir}/libgifutil.so
%attr(755,root,root) %{_libdir}/libungif.so
%{_includedir}/gif_lib.h
%{_includedir}/gif_util.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libgif.a
%{_libdir}/libgifutil.a
%{_libdir}/libungif.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gif2rgb
%attr(755,root,root) %{_bindir}/gifbuild
%attr(755,root,root) %{_bindir}/gifclrmp
%attr(755,root,root) %{_bindir}/giffix
%attr(755,root,root) %{_bindir}/giftext
%attr(755,root,root) %{_bindir}/giftool
%{_mandir}/man1/gif2rgb.1*
%{_mandir}/man1/gifbuild.1*
%{_mandir}/man1/gifclrmp.1*
%{_mandir}/man1/giffix.1*
%{_mandir}/man1/giftext.1*
%{_mandir}/man1/giftool.1*
%{_mandir}/man7/giflib.7*
